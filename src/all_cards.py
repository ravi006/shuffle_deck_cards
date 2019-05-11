

class Cards(object):

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __str__(self):
        result = self.face
        result += ' of '.join(self.suit)
        return self.face + " of " + self.suit
