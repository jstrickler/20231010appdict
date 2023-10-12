# from MODULE import CLASS
from carddeck import CardDeck
from jokerdeck import JokerDeck

import carddeck
d3 = carddeck.CardDeck("Tom")

d1 = CardDeck("Freddy")   # CardDeck.__init__(...)
print(f"d1: {d1}")

# print(f"d1._cards: {d1._cards}")  # NAUGHTY
# print(f"d1._cards[0].suit: {d1._cards[0].suit}")
print()



d1.shuffle()
print(f"d1.cards: {d1.cards}")

for i in range(5):
    card = d1.draw()
    print(f"card: {card}")
    

#  card = d1.draw()

d2 = CardDeck('Esmeralda')
print(f"len(d1): {len(d1)}")
print(f"len(d2): {len(d2)}")
print(f"d1.dealer: {d1.dealer}")
print(f"d2.dealer: {d2.dealer}")

d1.dealer = "Jackie"
print(f"d1.dealer: {d1.dealer}")

j = JokerDeck("Brenda")
j.shuffle()
print(f"j.cards: {j.cards}")
print()
j.play()