import re

commands_patterns = {
    '^\$create\s[a-zA-Z0-9_.-]+': 'create_playlist',
    '^\$add\s-p\s[a-zA-Z0-9_.-]+\s-l\s((http|https)://)?(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=])*': 'add_song'
}

def create_playlist(msg):
    playlist_name = msg.split(' ')[1]
    print(playlist_name)


def search(msg):
    patterns = list(commands_patterns.keys())
    for pattern in patterns:
        pattern_compiled = re.compile(pattern)
        if pattern_compiled.search(fr'{msg}') != None:
            command_value = commands_patterns[pattern]
            eval(f'{command_value}("{msg}")')
            print(pattern_compiled.search(fr'{msg}'))
