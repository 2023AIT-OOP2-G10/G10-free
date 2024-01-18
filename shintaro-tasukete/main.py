from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

# グローバル変数として選ばれた数字とPNGを初期化
selected_numbers = []
selected_pngs = []

# トランプの種類判別のための数字 Clovers 0-12 Diamonds 13-25 hearts 26-38 spades 39-51
trump_numbers = list(range(52))

# トランプ画像の名前を格納
png_Clovers = ["Clover_13.png", "Clover_1.png", "Clover_2.png", "Clover_3.png",
               "Clover_4.png", "Clover_5.png", "Clover_6.png", "Clover_7.png",
               "Clover_8.png", "Clover_9.png", "Clover_10.png", "Clover_11.png",
               "Clover_12.png"]
png_Diamonds = ["Diamond_13.png", "Diamond_1.png", "Diamond_2.png", "Diamond_3.png",
                "Diamond_4.png", "Diamond_5.png", "Diamond_6.png", "Diamond_7.png",
                "Diamond_8.png", "Diamond_9.png", "Diamond_10.png", "Diamond_11.png",
                "Diamond_12.png"]
png_hearts = ["heart_13.png", "heart_1.png", "heart_2.png", "heart_3.png",
              "heart_4.png", "heart_5.png", "heart_6.png", "heart_7.png",
              "heart_8.png", "heart_9.png", "heart_10.png", "heart_11.png",
              "heart_12.png"]
png_spades = ["spade_13.png", "spade_1.png", "spade_2.png", "spade_3.png",
              "spade_4.png", "spade_5.png", "spade_6.png", "spade_7.png",
              "spade_8.png", "spade_9.png", "spade_10.png", "spade_11.png",
              "spade_12.png"]


def trumps(selected_numbers, selected_pngs):
    while True:
        selected = random.choice(trump_numbers)
        # 同じ数が選ばれていないか判定
        if len(selected_numbers) == 0:
            selected_numbers.append(selected)
            # 13で割った後の値(0〜4)と余りでトランプを判別する
            # Clovers 0-12  Diamonds 13-25 hearts 26-38 spades 39-51
            # 割った余りがゼロの時13とする ex 14=Diamond 1 ,13=Diamond 13
            suit = selected // 13
            number = selected % 13
            print(suit)
            print(selected)
            print(number)
            if suit == 0:
                selected_pngs.append(png_Clovers[number])
            elif suit == 1:
                selected_pngs.append(png_Diamonds[number])
            elif suit == 2:
                selected_pngs.append(png_hearts[number])
            elif suit == 3:
                selected_pngs.append(png_spades[number])
            break
        elif len(selected_numbers) > 0:
            if selected not in selected_numbers:
                selected_numbers.append(selected)
                #13で割った後の値(0〜4)と余りでトランプを判別する
                # Clovers 0-12  Diamonds 13-25 hearts 26-38 spades 39-51
                # 割った余りがゼロの時13とする ex 14=Diamond 1 ,13=Diamond 13
                suit = selected // 13
                number = selected % 13
                print(suit)
                print(selected)
                print(number)
                if suit == 0:
                    selected_pngs.append(png_Clovers[number])
                elif suit == 1:
                    selected_pngs.append(png_Diamonds[number])
                elif suit == 2:
                    selected_pngs.append(png_hearts[number])
                elif suit == 3:
                    selected_pngs.append(png_spades[number])
                break

    return selected_numbers, selected_pngs


@app.route('/')
def start():
    return render_template('start.html')


@app.route('/blackjack_play', methods=['GET', 'POST'])
def blackjack_play():
    global selected_numbers, selected_pngs
    trumps_data = trumps(selected_numbers, selected_pngs)
    trumps_data2 = trumps(trumps_data[0], trumps_data[1])
    trumps_data3 = trumps(trumps_data2[0], trumps_data2[1])
    return render_template('blackjack.html',
                           selected_numbers=trumps_data3[0],
                           selected_pngs=trumps_data3[1])

@app.route('/blackjack', methods=['GET', 'POST'])
def blackjack():
    global selected_numbers, selected_pngs
    trumps_data = trumps(selected_numbers, selected_pngs)
    trumps_data2 = trumps(trumps_data[0], trumps_data[1])
    trumps_data3 = trumps(trumps_data2[0], trumps_data2[1])
    return render_template('blackjack.html',
                           selected_numbers=trumps_data3[0],
                           selected_pngs=trumps_data3[1])

if __name__ == '__main__':
    app.run(debug=True, port=5001)
