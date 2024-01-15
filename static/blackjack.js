        document.getElementById('start-game').addEventListener('click', () => playerAction('start'));
        document.getElementById('hit').addEventListener('click', () => playerAction('hit'));
        document.getElementById('stand').addEventListener('click', () => playerAction('stand'));

        function playerAction(action) {
            fetch(`/blackjack/${action}`, { method: 'POST' })
                .then(response => response.json())
                .then(data => updateGameView(data))
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

            playerHandDiv.innerHTML = 'プレイヤーの手札: ' + data.player_hand.map(cardToString).join(', ');
            dealerHandDiv.innerHTML = 'ディーラーの手札: ' + data.dealer_hand.map(cardToString).join(', ');

            if (data.game_over) {
                let resultMessage = 'ゲーム終了！ ';
                resultMessage += data.winner === 'player' ? 'プレイヤーの勝利！' :
                                 data.winner === 'dealer' ? 'ディーラーの勝利！' :
                                 '引き分け！';
                gameResultDiv.innerHTML = resultMessage;
            } else {
                gameResultDiv.innerHTML = '';
            }
        }

        function cardToString(card) {
            return `${card.Value} of ${card.Suit}`;
        }