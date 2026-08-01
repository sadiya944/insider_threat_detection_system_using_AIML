import sqlite3
import bcrypt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "insider_threat.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

# Create admin user
username = "admin"
password = "admin123"
role = "Admin"

hashed_password = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
).decode()

cursor.execute("""
INSERT OR IGNORE INTO users (username, password, role)
VALUES (?, ?, ?)
""", (username, hashed_password, role))

conn.commit()
conn.close()

print("Database created successfully!")
print("Username: admin")
print("Password: admin123")
