import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = os.getenv('DB_HOST'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database = os.getenv('DB_NAME')
        )
        self.cursor = self.connection.cursor()

    def insert_playlist(self,playlist):
        sql_query = f"INSERT INTO playlists (playlist) VALUES ('{playlist}')"
        self.cursor.execute(sql_query)
        self.connection.commit()

db = Database()
