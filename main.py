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
    list_all_artists()
    print('Refer to the list and enter artist\'s ID to display all of their artwork')
    artistID = int(input('Please enter the artist ID: '))
    rows = db.get_all_artwork_by_artist(artistID)
    for row in rows:
        print(row)

def list_all_artists():
    # TODO function to list all artists by name
    a = 1

def add_new_artwork():
    while True:
        try:
            title = input('Enter artwork\'s title: ')
            price = round(float(input('Enter artwork\'s price: ', 2)))
            available = input('Artwork is currently available (y/n)? ')
            # TODO turn y into 1 n into 0, mind cases
            # print artist's names and id's
            artistID = input('Enter artist\'s ID: ')

            break
        except Exception as e:
            print(e)
    artwork = Artwork(title, price, available, artistID)
    added = db.add_artwork(artwork)

    if added:
        print('Artwork added')
    else:
        print('ERROR - Add artwork error')

def delete_artwork():
    delete_artwork = ''


def change_availibility_of_artwork():
    artworkID = input('Enter artwork\'s ID: ')

if __name__ == '__main__':
    main()