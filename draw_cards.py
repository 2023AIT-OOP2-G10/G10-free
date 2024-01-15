def draw_cards(deck, num_cards=1):
    if num_cards > len(deck):
        raise ValueError('Not enough cards in the deck')

    cards = []
    for _ in range(num_cards):
        cards.append(deck.pop())

    return cards
