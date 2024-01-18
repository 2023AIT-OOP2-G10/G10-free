from flask import Flask, request, render_template
import random  # ランダムデータ作成のためのライブラリ
import datetime
from blackjack import blackjack_bp

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('start.html')


app.register_blueprint(blackjack_bp)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(port=5001)
