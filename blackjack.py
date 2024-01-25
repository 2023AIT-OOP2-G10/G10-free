from flask import Blueprint,Flask, request,jsonify,render_template
from card_utils import create_deck
from draw_cards import draw_cards
from calculate_hand_value import calculate_hand_value
from calculate_score import calculate_score
from store_json import store_json
import random

app = Flask(__name__)
blackjack_bp = Blueprint('blackjack', __name__)

game_state = {
    'deck': [],
    'player_hand': [],
    'dealer_hand': [],
    'game_over': False,
    'winner': None,
    'name': "名無しプレイヤー",
    'score':0,
}

@blackjack_bp.route('/blackjack', methods=["GET"])
def start():
    game_state['name'] = request.args.get('name',"名無しプレイヤー")
    return render_template('blackjack_test.html',name=game_state['name'])

# start
@blackjack_bp.route('/blackjack/start', methods=['GET', 'POST'])
def start_game():
    game_state['deck'] = create_deck()
    random.shuffle(game_state['deck'])
    game_state['player_hand'] = draw_cards(game_state['deck'], 2)
    game_state['dealer_hand'] = draw_cards(game_state['deck'], 2)
    game_state['game_over'] = False
    game_state['winner'] = None
    return jsonify(game_state)


# ヒット
@blackjack_bp.route('/blackjack/hit', methods=['POST'])
def player_hit():
    if game_state['game_over']:
        return jsonify({'error': 'Game is already over'})

    game_state['player_hand'] += draw_cards(game_state['deck'], 1)
    player_total = calculate_hand_value(game_state['player_hand'])

    if player_total > 21:  # バーストチェック
        game_state['game_over'] = True
        game_state['winner'] = 'dealer'
        store_json(game_state['name'],game_state['score'])

        return jsonify(game_state)

    return jsonify(game_state)


# スタンド
@blackjack_bp.route('/blackjack/stand', methods=['POST'])
def player_stand():
    if game_state['game_over']:
        return jsonify({'error': 'Game is already over'})

    # ディーラー
    while calculate_hand_value(game_state['dealer_hand']) < 17:
        game_state['dealer_hand'] += draw_cards(game_state['deck'], 1)

    # 勝敗の判定
    player_total = calculate_hand_value(game_state['player_hand'])
    dealer_total = calculate_hand_value(game_state['dealer_hand'])

    if dealer_total > 21 or player_total > dealer_total:
        game_state['winner'] = 'player'
        game_state['score']=calculate_score(game_state['player_hand'],game_state['score'])
    elif dealer_total > player_total:
        game_state['winner'] = 'dealer'
    else:
        game_state['winner'] = 'push'

    game_state['game_over'] = True
    store_json(game_state['name'],game_state['score'])

    return jsonify(game_state)

# リセット 追加
@blackjack_bp.route('/blackjack/reset', methods=['POST'])
def reset_game():
    game_state['deck'] = []
    game_state['player_hand'] = []
    game_state['dealer_hand'] = []
    game_state['game_over'] = False
    game_state['winner'] = None
    game_state['name'] = "名無しプレイヤー"
    game_state['score'] = 0
    return jsonify(game_state)

@blackjack_bp.route('/blackjack/result', methods=['POST'])
def submit_game_result():
    data = game_state
    # データ処理（スコア計算）
    # 既存のテンプレートを使用してHTMLをレンダリング
    return render_template('result.html',name=game_state['name'],winner=game_state['winner'],score=game_state['score'])