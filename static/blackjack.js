document.getElementById('start-game').addEventListener('click', () => playerAction('start'));
document.getElementById('hit').addEventListener('click', () => playerAction('hit'));
document.getElementById('stand').addEventListener('click', () => playerAction('stand'));
document.getElementById('reset-game').addEventListener('click', resetGame);  // スタート画面に戻るをイベントリスナーを追加
document.addEventListener('DOMContentLoaded', function() {
    // ゲームを保存するボタンのイベントリスナー
    document.getElementById('save-game').addEventListener('click', function() {
        saveGame();
    });
    // ゲームを読み込むボタンのイベントリスナー
    document.getElementById('load-game').addEventListener('click', function() {
        loadGame();
    });
 });

function playerAction(action) {
    fetch(`/blackjack/${action}`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateGameView(data);
            updateCardImages(data);
        })
        .catch(error => console.error('Error:', error));
}



function updateGameView(data) {
    if (data.error) {
        alert(data.error);
        return;
    }

    const playerHandDiv = document.getElementById('player-hand');
    const dealerHandDiv = document.getElementById('dealer-hand');
    const gameResultDiv = document.getElementById('game-result');

    playerHandDiv.innerHTML = data.player_hand.map(cardToString).join(', ');
    dealerHandDiv.innerHTML = data.dealer_hand.map(cardToString).join(', ');

    if (data.game_over) {
        let resultMessage = 'ゲーム終了！ ';
        resultMessage += data.winner === 'player' ? 'プレイヤーの勝利！' :
            data.winner === 'dealer' ? 'ディーラーの勝利！' :
                '引き分け！';
        gameResultDiv.innerHTML = resultMessage;

        // 追加: ゲームが終了した場合にリセットボタンを表示
        const resetButton = document.getElementById('reset-game');
        resetButton.style.display = 'block';

    } else {
        gameResultDiv.innerHTML = '';
    }
}
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

function saveGame() {
    const gameData = {/* ゲーム状態のデータ */};
    // 例: { player_hand: [...], dealer_hand: [...], ... }
    fetch('/save_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(gameData),
    })
    .then(response => response.json())
    .then(data => console.log(data.message))
    .catch(error => console.error('Error:', error));
}


function loadGame() {
    fetch('/load_game')
        .then(response => response.json())
        .then(data => {
            // ゲーム状態を更新するための関数
            updateGameView(data);
            updateGameState(data);
            updateCardImages(data);
        })
        .catch(error => console.error('Error:', error));
}

function cardToString(card) {
    return `<img src="/static/${card.Suit}_${card.Value}.png" alt="${card.Suit} ${card.Value}" width="100">`;
}