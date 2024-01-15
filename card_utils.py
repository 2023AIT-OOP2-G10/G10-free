def create_deck():
    suits = ["heart", "Clover", "Diamond", "spade"]
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    deck = []
    for suit in suits:
        for value in values:
            deck.append({'Value': value, 'Suit': suit})
    return deck
