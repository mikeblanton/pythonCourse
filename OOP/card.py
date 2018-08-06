# Each instance of Card  should have a suit
#  ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value
#  ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should return the card's value and suit
#  (e.g. "A of Clubs", "J of Diamonds", etc.)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
