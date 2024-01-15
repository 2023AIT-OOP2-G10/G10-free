from flask import Flask, render_template, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'
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


def trumps():
    selected_numbers = session.get('selected_numbers', [])
    selected_images = session.get('selected_images', [])

    while True:
        selected = random.choice(trump_numbers)

        if selected not in selected_numbers:
            selected_numbers.append(selected)
            suit = selected // 13
            number = selected % 13

            if suit == 0:
                selected_images.append(clovers_images[number])
            elif suit == 1:
                selected_images.append(diamonds_images[number])
            elif suit == 2:
                selected_images.append(hearts_images[number])
            elif suit == 3:
                selected_images.append(spades_images[number])

            break

    session['selected_numbers'] = selected_numbers
    session['selected_images'] = selected_images

    return selected_numbers, selected_images


@app.route('/')
def start():
    # selected_numbersおよびselected_imagesの初期化
    session.pop('selected_numbers', None)
    session.pop('selected_images', None)
    return render_template('start.html')


@app.route('/blackjack', methods=['GET', 'POST'])
def blackjack():
    trumps_data = trumps()
    return render_template('blackjack.html',
                           selected_numbers=trumps_data[0],
                           selected_images=trumps_data[1])


if __name__ == '__main__':
    app.run(debug=True)
