from sentence_transformers import SentenceTransformer
import faiss

class EmbeddingManager:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.IndexFlatL2(768)  # Assuming 768-dimensional embeddings

    def generate_embeddings(self, texts):
        """
        generates embeddings for a list of texts
        """
        embeddings = self.model.encode(texts)
        return embeddings

    def build_index(self, embeddings):
        """
        builds a Faiss index for fast nearest neighbor search
        """
        self.index.add(embeddings)

    def search(self, query_embedding, k=5):
        """
        Searches the index for the k nearest neighbors
        query_embedding: The embedding of the query
        k: The number of nearest neighbors to retrieve
        """
        distances, indices = self.index.search(query_embedding.reshape(1, -1), k)
        return distances, indices