def create_deck():
    suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = []
    for suit in suits:
        for value in values:
            deck.append({'Value': value, 'Suit': suit})
    return deck
