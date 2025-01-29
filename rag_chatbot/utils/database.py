import mysql.connector
from dotenv import load_dotenv
import os

class Database:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        db_host = os.environ.get('DB_HOST', 'localhost') 
        db_user = os.environ.get('DB_USER') 
        db_password = os.environ.get('DB_PASSWORD') 
        db_name = os.environ.get('DB_NAME')

        self.conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        self.cursor = self.conn.cursor()

    def insert_chat_history(self, role, content):
        """
        insert a new chat message into the database
        """
        sql = "INSERT INTO chat_history (role, content) VALUES (%s, %s)"
        val = (role, content)
        self.cursor.execute(sql, val)
        self.conn.commit()

    def get_chat_history(self):
        """
        retrieves all chat history from the database
        """
        sql = "SELECT role, content FROM chat_history"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def close(self):
        self.conn.close()