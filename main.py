from flask import Flask, request, render_template
from blackjack import blackjack_bp
import json

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('start.html')


@app.route('/sorted_scores')
def score():
    with open('store.json', 'r') as file:
        data = json.load(file)

    # scoreの降順にソート
    sorted_data = sorted(data, key=lambda x: x['score'], reverse=True)

    return render_template('score.html', data=sorted_data[:10])


@app.route('/sorted_scores/latest')
def latest():
    with open('store.json', 'r') as file:
        data = json.load(file)

    # 直近10個のスコアを取得
    reversed_data = list(reversed(data))
    return render_template('score_latest.html', data=reversed_data[:10])


app.register_blueprint(blackjack_bp)

# blackjack.pyに記述
#
# @app.route('/result')
# def result():
#     return render_template('result.html')

if __name__ == '__main__':
    app.run(port=5001)
