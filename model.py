class Artist:
    def __init__(self, name, email):
        self.name = name
        self.email = email


    def __str__(self):
        return f'{self.name}, {self.email}'


class Artwork:

    def __init__(self, artist, title, price, available=False):
        self.artist = artist
        self.title = title
        self.price = price
        self.available = available

    def __str__(self):
        return f'{self.artist}, {self.title}, {self.price}, {self.available}'
