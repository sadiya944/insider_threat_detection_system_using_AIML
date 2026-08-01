import sqlite3
import bcrypt

password = bcrypt.hashpw(
    "admin123".encode(),
    bcrypt.gensalt()
).decode()

conn = sqlite3.connect("insider_threat.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO users(username,password,role)
VALUES(?,?,?)
""",(
    "admin",
    password,
    "Admin"
))

conn.commit()
conn.close()

print("Admin Created")
