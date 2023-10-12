from carddeck import CardDeck, Card

class Game:
    def play(self):
        print("playing...")


class JokerDeck(Game, CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call _make_deck in CardDeck
        for i in range(2):
            card = Card('** JOKER **', None)
            self._cards.append(card)

