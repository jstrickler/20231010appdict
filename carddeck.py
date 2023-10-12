import random

class Card:

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    @property
    def rank(self):  #  getter property
        return self._rank
    
    # def get_rank():
    #     return this._rank

    @property
    def suit(self):
        return self._suit

    # human-friendly string
    def __str__(self):
        return f"{self.rank}-{self.suit}"

    # code-friendly string
    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'


# c = Card("2", "Spades"")

#   "dunder x"  ==>  "__x__"

class CardDeck:
    # class variables
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    # c = CardDeck() calls CardDeck.__init__()
    def __init__(self, dealer):
        """Constructor -- 'self' is new object """
        
        # instance variable
        self.dealer = dealer  # dealer name
        self._cards = None     # will be populated by _make_deck()

        # call private instance method
        self._make_deck()

    def _make_deck(self):
        self._cards = []  # adding private instance variable
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)


    @property
    def dealer(self): # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, value):  # setter property
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")

    @property  # converts from METHOD to PROPERTY 
    def cards(self):  # public getter
        return tuple(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __str__(self):  # responds to str(obj)
        return f"<Card Deck>"

    def __repr__(self):
        return f"CardDeck()"

    def __len__(self):   # responds to len(obj)
        return len(self._cards)
    

if __name__ == "__main__":
    c = Card('2', 'Clubs')
    print(f"c: {c}")
    
    print(f"repr(c): {repr(c)}")
    
    print(f"c.rank: {c.rank}")
    print(f"c.suit: {c.suit}")


