from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
app = Flask(__name__)
CORS(app)

# Database banao
def init_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY,
                  kya TEXT,
                  kitna REAL,
                  category TEXT)''')
    conn.commit()
    conn.close()

# Sab expenses lao
@app.route('/expenses', methods=['GET'])
def get_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('SELECT * FROM expenses')
    rows = c.fetchall()
    conn.close()
    expenses = [{'id': r[0], 'kya': r[1], 'kitna': r[2], 'category': r[3]} for r in rows]
    return jsonify(expenses)

# Naya expense add karo
@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('INSERT INTO expenses (kya, kitna, category) VALUES (?, ?, ?)',
              (data['kya'], data['kitna'], data['category']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Expense add ho gaya!'}), 201

# Expense delete karo
@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Expense delete ho gaya!'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)