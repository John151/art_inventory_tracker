"""Gallery artwork cateloge program
    add modify or delete artists, artwork to database"""
import SQLDatabase as db
from model import Artist, Artwork

def main():
    setup()
    add_new_artist()

def setup():
    db.create_tables()

def add_new_artist():
    name = input('Enter artist\'s name: ')
    email = input('Enter artist\'s email address: ')
    artist = Artist(name, email)
    added = db.add_artist(artist)

    if added:
        print('Artist added')
    else:
        print('ERROR - Add artist error')


def search_for_artwork_by_artist():
    # TODO function to search for artwork by artist name
    a = 1

def list_all_artists():
    # TODO function to list all artists by name
    a = 1

def add_new_artwork():
    # TODO function to add new artwork, need artist name
    a = 1

def delete_artwork():
    #  TODO function to delete an artwork
    a = 1

def change_availibility_of_artwork():
    # TODO change availibility
    a = 1

if __name__ == '__main__':
    main()