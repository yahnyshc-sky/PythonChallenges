from flask import Flask, request, jsonify
import random

app = Flask(__name__)

choices = ['rock', 'paper', 'scissors']

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
    
@app.route('/play', methods=['POST'])

def play_game():
    data = request.get_json()
    user_choice = data.get('choice')
    if user_choice not in choices:
        return jsonify({'error': 'Invalid choice. Please choose rock, paper, or scissors.'}), 400
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })

@app.route('/', methods=['GET'])
def index():
    return '''
    <html>
    <head><title>Rock Paper Scissors</title></head>
    <body>
        <h1>Play Rock Paper Scissors!</h1>
        <form id="rps-form">
            <label>Choose:</label>
            <select name="choice" id="choice">
                <option value="rock">Rock</option>
                <option value="paper">Paper</option>
                <option value="scissors">Scissors</option>
            </select>
            <button type="submit">Play</button>
        </form>
        <div id="result"></div>
        <script>
        document.getElementById('rps-form').onsubmit = async function(e) {
            e.preventDefault();
            const choice = document.getElementById('choice').value;
            const response = await fetch('/play', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({choice})
            });
            const data = await response.json();
            document.getElementById('result').innerHTML =
                response.ok ? `<p>You chose: ${data.user_choice}<br>Computer chose: ${data.computer_choice}<br><b>${data.result}</b></p>`
                : `<p style='color:red;'>${data.error}</p>`;
        };
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)