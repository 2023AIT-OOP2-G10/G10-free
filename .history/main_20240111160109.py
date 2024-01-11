from flask import Flask, request, render_template
import random  # ランダムデータ作成のためのライブラリ
import datetime

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('start.html')


if __name__ == '__main__':
    app.run()
