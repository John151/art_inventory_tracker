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
        print('Error adding artist', e)
        return False

# show all artwork for 1 artist that's available
def get_all_artwork_by_artist(artistID):
    get_all_artwork_by_one_artist = 'SELECT * FROM artwork WHERE artistID = ?'
    conn = sqlite3.connect(db_path)
    results = conn.execute(get_all_artwork_by_one_artist, (artistID, )).fetchall()
    return results

# show all artists
def get_all_artists():
    get_all_artists = 'SELECT * FROM artists'
    conn = sqlite3.connect(db_path)
    rows = conn.execute(get_all_artists).fetchall()
    return rows

# delete artist
def delete_artist():
    pass

# add artwork
def add_artwork(artwork):
    add_new_artwork = 'INSERT INTO artwork VALUES (?, ?, ?, ?)'
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute(add_new_artwork, (artwork.title, artwork.price, artwork.available, artwork.artistID))

# delete artwork
def delete_artwork(artworkID):
    delete_an_artwork = 'DELETE FROM artwork WHERE artworkID = ?'
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute(delete_an_artwork, (artworkID, ))
        conn.close()
        return True
    except Exception as e:
        print('Delete artwork error', e)

# change availability of artwork
def toggle_artwork_availability(artwork):
    change_availability = 'UPDATE artwork SET available = ? WHERE artworkID = ?'
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute(change_availability, (artwork.available, artwork.artworkID))
        conn.close()
        return True
    except Exception as e:
        print('Error changing artwork availability', e)
        return False