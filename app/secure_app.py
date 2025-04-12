from flask import Flask, render_template, request, jsonify
from app.database import init_db, get_db_connection

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    c.execute(query, (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        return render_template('result.html', message=f"Welcome back, {user[1]}!")
    else:
        return render_template('result.html', message="Login failed.")

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/search_results', methods=['POST'])
def search_results():
    term = request.form['term']

    conn = get_db_connection()
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username LIKE ?"
    c.execute(query, (f"%{term}%",))
    results = c.fetchall()
    conn.close()

    return render_template('result.html', message=f"Search Results: {results}")

@app.route('/blind-login', methods=['POST'])
def blind_login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    c.execute(query, (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        return "Success"
    else:
        return "Failure"

@app.route('/admin')
def admin():
    username = request.args.get('username')

    conn = get_db_connection()
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND role = 'admin'"
    c.execute(query, (username,))
    user = c.fetchone()
    conn.close()

    if user:
        return render_template('result.html', message=f"Welcome, Admin {user[1]}")
    else:
        return render_template('result.html', message="Access denied.")

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = get_db_connection()
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    c.execute(query, (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        return jsonify({"status": "success", "message": f"Welcome {user[1]}"})
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401