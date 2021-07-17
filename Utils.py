import re
from Database import *

class Utils:
    def __init__(self, db_conn=Database()):
        self.commands_patterns = {
            '^\$create\s[a-zA-Z0-9_.\- ]+$': 'create_playlist',
            '^\$add\s-p\s[a-zA-Z0-9_.\- ]+\s-s\s[a-zA-Z0-9_.\- ]+\s-l\s((http|https)://)'
                '?(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}'
                '\\b([-a-zA-Z0-9@:%._\\+~#?&//=])*': 'add_song',
            '^\$list$': 'list_playlists',
            '^\$list\s[a-zA-Z0-9_.\- ]+$': 'list_playlist_data'
        }
        self.db_conn = db_conn
        self.to_send_msgs = []
    # FECTH ALL SONGS IN A GIVEN PLAYLIST
    def list_playlist_data(self, msg):
        playlist = msg.split(' ',1)[-1]
        self.to_send_msgs = self.db_conn.list_playlist(playlist)
    # FETCH PLAYLISTS
    def list_playlists(self, msg):
        playlists_data = self.db_conn.list_playlists()
        self.to_send_msgs = playlists_data
    # FILTER PLAYLIST NAME AND PASS IT TO DB MODEL
    def create_playlist(self, msg):
        playlist_name = msg.split(' ',1)[1]
        self.db_conn.insert_playlist(playlist_name)
    # FILTER SONG NAME AND PASS IT TO THE DB MODEL
    def add_song(self, msg):
        splitted_msg = msg.split(' ')
        song_link = splitted_msg[-1]
        song_name = ' '.join(splitted_msg[splitted_msg.index('-s')+1:splitted_msg.index('-l')])
        playlist_name = ' '.join(splitted_msg[splitted_msg.index('-p')+1:splitted_msg.index('-s')])
        self.db_conn.insert_song(song_name,playlist_name,song_link)
    # FIND THE MESSAGE PATTERN BASED ON THE REGEX IN THE CONSTRUCTOR
    def pattern_search(self, msg):
        patterns = list(self.commands_patterns.keys())
        for pattern in patterns:
            pattern_compiled = re.compile(pattern)
            if pattern_compiled.search(fr'{msg}') != None:
                command_value = self.commands_patterns[pattern]
                eval(f'self.{command_value}("{msg}")')
