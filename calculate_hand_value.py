def calculate_hand_value(hand):
    if not hand:
        return 0  # 空の手札の場合は0を返す

    total = 0
    ace_count = 0

    for card in hand:
        if card['Value'] in ['11', '12', '13']:
            total += 10
        elif card['Value'] == '1':
            ace_count += 1
            total += 11
        else:
            total += int(card['Value'])

    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1

    return total
