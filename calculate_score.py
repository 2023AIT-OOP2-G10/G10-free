def calculate_score(player_hand,score):
    if not player_hand:
        return 0  # 空の手札の場合は0を返す
    
    total =1
    for card in player_hand:
        total = int(card['Value'])*total

    score=int(score)+total
    return score