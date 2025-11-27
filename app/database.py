import sqlite3
from flask import current_app, g




def get_db():
db = getattr(g, '_database', None)
if db is None:
db = g._database = sqlite3.connect(current_app.config['DATABASE'])
db.row_factory = sqlite3.Row
return db




def close_db(e=None):
db = getattr(g, '_database', None)
if db is not None:
db.close()




def init_db(app):
# create users table if not exists
with app.app_context():
db = get_db()
db.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
)
''')
db.commit()




def add_user_if_not_exists(username, password):
db = get_db()
cur = db.execute('SELECT id FROM users WHERE username = ?', (username,))
if cur.fetchone() is None:
db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
db.commit()