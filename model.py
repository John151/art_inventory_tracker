class Artist:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.name}, {self.email}'


class Artwork:

    def __init__(self, title, price, available, artist):
        self.title = title
        self.price = price
        self.available = available
        self.artist = artist

    def __str__(self):
        if self.available == 1:
            available = 'Available'
        else:
            available = 'Not Available'
        return f'{self.artist}, {self.title}, {self.price}, {available}'
