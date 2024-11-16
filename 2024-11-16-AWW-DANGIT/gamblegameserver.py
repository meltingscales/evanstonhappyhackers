from flask import Flask, request, jsonify
import random
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
DATABASE = 'game.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create a users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            balance INTEGER
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')

    # Check if the username already exists
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    if user:
        conn.close()
        return jsonify({'error': 'Username already exists'}), 400

    # Add the new user
    cursor.execute('INSERT INTO users (username, balance) VALUES (?, ?)', (username, 100))
    conn.commit()
    conn.close()
    return jsonify({'message': f'Welcome {username}!', 'balance': 100})

@app.route('/play', methods=['POST'])
def gamble_with_weights():
    username = request.json.get('username')
    bet = request.json.get('bet')
    weights = request.json.get('w', [1, 1, 1])  # Default weights

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Check if the user exists
    cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        return jsonify({'error': 'User not found'}), 404

    balance = user[0]
    if balance < bet:
        conn.close()
        return jsonify({'error': 'Insufficient balance'}), 400

    # Validate weights
    if not isinstance(weights, list) or len(weights) != 3 or any(w <= 0 for w in weights):
        conn.close()
        return jsonify({'error': 'Invalid weights'}), 400

    # Normalize weights to calculate probabilities
    total_weight = sum(weights)
    probabilities = [w / total_weight for w in weights]
    result = random.choices(['win', 'lose', 'jackpot'], probabilities)[0]

    # Update balance based on the result
    if result == 'win':
        balance += bet
    elif result == 'lose':
        balance -= bet
    elif result == 'jackpot':
        balance += bet * 10

    cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (balance, username))
    conn.commit()
    conn.close()

    return jsonify({'result': result, 'balance': balance})

@app.route('/cashout', methods=['POST'])
def cashout():
    username = request.json.get('username')

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Check if the user exists
    cursor.execute('SELECT balance FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        return jsonify({'error': 'User not found'}), 404

    balance = user[0]
    cursor.execute('UPDATE users SET balance = 0 WHERE username = ?', (username,))
    conn.commit()
    conn.close()

    return jsonify({'message': f'You cashed out {balance}!', 'balance': 0})

if __name__ == '__main__':
    # Initialize the database
    init_db()
    app.run(debug=True)
