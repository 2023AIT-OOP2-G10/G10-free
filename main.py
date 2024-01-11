from  flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ
import datetime

app = Flask(__name__)

@app.route('/black_jack')
def uranai():
    return render_template('start_form.html')

if __name__ == '__main__':
    app.run()