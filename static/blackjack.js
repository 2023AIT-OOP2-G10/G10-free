document.getElementById('start-game').addEventListener('click', () => playerAction('start'));
document.getElementById('hit').addEventListener('click', () => {
    playerAction('hit');
    slideInCard('player-hand');
});
document.getElementById('stand').addEventListener('click', () => {
    playerAction('stand');
    slideInCard('dealer-hand');
});
document.getElementById('reset-game').addEventListener('click', resetGame);
document.getElementById('restartButton').addEventListener('click', restartGame);

function playerAction(action) {
    fetch(`/blackjack/${action}`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateGameView(data);
            updateCardImages(data);
        })
        .catch(error => console.error('Error:', error));
}

function slideInCard(elementId) {
    const cardContainer = document.getElementById(elementId);
    const cards = cardContainer.getElementsByClassName('card');

    // カードが右端からスライドインするアニメーションを適用
    for (let card of cards) {
        card.classList.add('slide-in-card');
    }

    // アニメーションが終了したらクラスを削除
    cards[0].addEventListener('animationend', function () {
        for (let card of cards) {
            card.classList.remove('slide-in-card');
        }
    });
}

function updateGameView(data) {
    if (data.error) {
        alert(data.error);
        return;
    }

    const playerHandDiv = document.getElementById('player-hand');
    const dealerHandDiv = document.getElementById('dealer-hand');
    const gameResultDiv = document.getElementById('game-result');

    playerHandDiv.innerHTML = data.player_hand.map(cardToString).join('');
    dealerHandDiv.innerHTML = data.dealer_hand.map(cardToString).join('');


    if (data.game_over) {
        let resultMessage = 'ゲーム終了！ ';
        resultMessage += data.winner === 'player' ? 'プレイヤーの勝利！' :
            data.winner === 'dealer' ? 'ディーラーの勝利！' :
                '引き分け！';
        gameResultDiv.innerHTML = resultMessage;

        // ゲームが終了した場合にリセットボタンを表示
        const resetButton = document.getElementById('reset-game');
        resetButton.style.display = 'block';

        // result追加
        submitGameResult(data);
    } else {
        gameResultDiv.innerHTML = '';
    }
}

// 既存の関数、リセットとリスタートの処理はそのままです

// 追加
function resetGame() {
    console.log('Reset button clicked!');  // デバッグメッセージ
    fetch('/blackjack/reset', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateGameView(data);
            // 追加: リセットボタンを非表示にする
            document.getElementById('reset-game').style.display = 'none';
        })
        .catch(error => console.error('Error:', error));

    // 追加: ゲームがリセットされたらスタート画面に戻る
    window.location.href = '/';
}

function restartGame() {
    console.log('restart button clicked!');  // デバッグメッセージ
    fetch('/blackjack/reset', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateGameView(data);
            // 追加: リセットボタンを非表示にする
            document.getElementById('reset-game').style.display = 'none';
        })
        .catch(error => console.error('Error:', error));

    // 追加: ゲームがリセットされたらゲーム画面に戻る
    window.location.href = '/blackjack';
}

function cardToString(card) {
    return `<img src="/static/${card.Suit}_${card.Value}.png" alt="${card.Suit} ${card.Value}" width="100">`;
}

// result画面呼び出し
function submitGameResult(gameData) {
    fetch('/blackjack/result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(gameData)
    })
        .then(response => response.text())
        .then(html => {
            document.body.innerHTML = html;
        })
        .catch(error => console.error('Error:', error));
}