import sqlite3
from flask import g

DATABASE = 'DbCleanSa.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()