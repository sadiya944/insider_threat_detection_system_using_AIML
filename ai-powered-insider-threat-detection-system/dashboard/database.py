import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "insider_threat.db")

print("DATABASE PATH:", DB_PATH)
print("DATABASE EXISTS:", os.path.exists(DB_PATH))

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
