from flask import Flask, request, jsonify
from utils import preprocessing, embedding, database
from models import model
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv() 
db_host = os.environ.get('DB_HOST', 'localhost') 
db_user = os.environ.get('DB_USER') 
db_password = os.environ.get('DB_PASSWORD') 
db_name = os.environ.get('DB_NAME')

# Initialize database
db = database.Database(
    host=db_host, 
    user=db_user, 
    password=db_password, 
    database=db_name
)

# Load corpus and create embeddings
with open('data/corpus.txt', 'r') as f:
    corpus = f.read()

corpus_chunks = preprocessing.chunk_text(corpus)
embedding_manager = embedding.EmbeddingManager()
corpus_embeddings = embedding_manager.generate_embeddings(corpus_chunks)
embedding_manager.build_index(corpus_embeddings)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get('query')

    if user_query:
        query_embedding = embedding_manager.model.encode([user_query])[0]
        _, indices = embedding_manager.search(query_embedding)
        retrieved_chunks = [corpus_chunks[i] for i in indices[0]]

        answer = model.generate_answer(user_query, retrieved_chunks)

        db.insert_chat_history('user', user_query)
        db.insert_chat_history('system', answer)

        return jsonify({'answer': answer})
    else:
        return jsonify({'error': 'No query provided'}), 400

@app.route('/history', methods=['GET'])
def get_history():
    history = db.get_chat_history()
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)