import sqlite3
from config import db_path

# create tables
def create_tables():
    try:
        # artist table
        create_artist_table = """ 
            CREATE TABLE IF NOT EXISTS artists (
            artistID INTEGER PRIMARY KEY, 
            name TEXT NOT NULL,
            email TEXT
            )"""
        # artwork table
        create_artwork_table = """
            CREATE TABLE IF NOT EXISTS artwork (
            artworkID INTEGER PRIMARY KEY, 
            title TEXT,
            price REAL,
            available INTEGER,
            artistID INTEGER,
            FOREIGN KEY (artistID) REFERENCES artist(artistID)
            )"""
        with sqlite3.connect(db_path) as conn:
            conn.execute(create_artist_table)
            conn.execute(create_artwork_table)
        conn.close()
    except Exception as e:
        print('Error creating table', e)


# add artist
def add_artist(artist):
    add_new_artist = 'INSERT INTO artists VALUES (?, ?)'
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute(add_new_artist, (artist.name, artist.email))
        conn.close()
        return True
    except Exception as e:
        print('some error', e)
        return False

# show all artists
def get_all_artists():
    pass

# delete artist
def delete_artist():
    pass

# add artwork
def add_artwork():
    pass

# show all artwork for 1 artist
def get_artwork():
    pass

# show all artwork for all artists
def get_all_artwork():
    pass

# delete artwork
def delete_artwork():
    pass
