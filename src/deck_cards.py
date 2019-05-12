
import random

from src.all_cards import Cards


class DeckOfCard(object):

    def __init__(self):
        self.faces = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.card_number = 0
        self.deck = self.get_deck(self.faces, self.suits)

    def shuffle_cards(self):
        self.card_number = 0
        for i in range(0, 52):
            tmp = self.deck[i]
            second = random.randrange(0, 52, 1)
            self.deck[i] = self.deck[second]
            self.deck[second] = tmp

    def deal_card(self):
        if self.card_number < 52:
            n = self.card_number
            self.card_number += 1
            return self.deck[n]
        else:
            return "None"

    @staticmethod
    def get_deck(faces, suits):
        decks = []
        for i in range(0, 52):
            decks.append(Cards(faces[i % 13], suits[i // 13]))
        return decks


if __name__ == '__main__':
    deck_cards = DeckOfCard()
    deck_cards.shuffle_cards()

    for i in range(0, 13):

        print('{!s:10}    {!s:10}   {!s:10}   {!s:1}'.format(deck_cards.deal_card(), deck_cards.deal_card(),
                                                             deck_cards.deal_card(), deck_cards.deal_card()))

