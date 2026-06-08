from flask import Flask, jsonify, request

app = Flask(__name__)

# Expenses store karne ke liye list
expenses = []

# Home route
@app.route('/')
def home():
    return 'Expense Tracker API chal raha hai!'

# Sab expenses lao
@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses)

# Naya expense add karo
@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    expenses.append(data)
    return jsonify({'message': 'Expense add ho gaya!'}), 201

if __name__ == '__main__':
    app.run(debug=True)