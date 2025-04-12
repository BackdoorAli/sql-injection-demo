import sqlite3
import os

def init_db(db_path='data/users.db'):
    if not os.path.exists('data'):
        os.makedirs('data')

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL)''')
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    c.execute("INSERT INTO users (username, password) VALUES ('user', 'password')")
    conn.commit()
    conn.close()

def get_db_connection():
    return sqlite3.connect('data/users.db')