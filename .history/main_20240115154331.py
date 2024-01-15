from flask import Flask, request, render_template
import random  # ランダムデータ作成のためのライブラリ
import datetime
from blackjack import blackjack_bp

app = Flask(__name__)

trump_numbers = list(range(52))

clovers_images = ["Clover_13.png", "Clover_1.png", "Clover_2.png", "Clover_3.png",
                  "Clover_4.png", "Clover_5.png", "Clover_6.png", "Clover_7.png",
                  "Clover_8.png", "Clover_9.png", "Clover_10.png", "Clover_11.png",
                  "Clover_12.png"]
diamonds_images = ["Diamond_13.png", "Diamond_1.png", "Diamond_2.png", "Diamond_3.png",
                   "Diamond_4.png", "Diamond_5.png", "Diamond_6.png", "Diamond_7.png",
                   "Diamond_8.png", "Diamond_9.png", "Diamond_10.png", "Diamond_11.png",
                   "Diamond_12.png"]
hearts_images = ["heart_13.png", "heart_1.png", "heart_2.png", "heart_3.png",
                 "heart_4.png", "heart_5.png", "heart_6.png", "heart_7.png",
                 "heart_8.png", "heart_9.png", "heart_10.png", "heart_11.png",
                 "heart_12.png"]
spades_images = ["spade_13.png", "spade_1.png", "spade_2.png", "spade_3.png",
                 "spade_4.png", "spade_5.png", "spade_6.png", "spade_7.png",
                 "spade_8.png", "spade_9.png", "spade_10.png", "spade_11.png",
                 "spade_12.png"]


@app.route('/')
def start():
    return render_template('start.html')


app.register_blueprint(blackjack_bp)

if __name__ == '__main__':
    app.run()
