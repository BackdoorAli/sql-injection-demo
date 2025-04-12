from flask import Flask, render_template, request
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
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("[!] Executing Query:", query)
    c.execute(query)
    user = c.fetchone()
    conn.close()

    if user:
        return render_template('result.html', message="Welcome back, {}!".format(user[1]))
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
    query = f"SELECT * FROM users WHERE username LIKE '%{term}%'"
    print("[!] Executing Query:", query)
    c.execute(query)
    results = c.fetchall()
    conn.close()

    return render_template('result.html', message=f"Search Results: {results}")