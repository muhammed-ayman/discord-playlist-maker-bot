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
    # CHECK IF PLAYLIST EXISTS
    def check_playlist(self, playlist_name):
        sql_query = f"""
            SELECT * FROM playlists WHERE playlist = '{playlist_name}'
        """
        self.cursor.execute(sql_query)
        if self.cursor.fetchone() != None:
            return True
        else:
            return False
    # CREATE PLAYLIST WITH {playlist} NAME
    def insert_playlist(self,playlist):
        if self.check_playlist(playlist):
            return
        sql_query = f"INSERT INTO playlists (playlist) VALUES ('{playlist}')"
        self.cursor.execute(sql_query)
        self.connection.commit()
    # INSERT A SONG IN THE GIVEN PLAYLIST IF EXISTS OR CREATE IT AND INSERT AFTERWARDS
    def insert_song(self, song, playlist, link):
        if not self.check_playlist(playlist):
            self.insert_playlist(playlist)
        sql_query = f"""
            INSERT INTO songs (song,playlist,link) VALUES ('{song}','{playlist}','{link}')
        """
        self.cursor.execute(sql_query)
        self.connection.commit()
