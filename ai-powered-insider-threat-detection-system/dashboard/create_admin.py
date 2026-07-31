import bcrypt
from database import get_connection

username = "admin"
password = "admin123"
port= 3307

hashed = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
).decode()

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
INSERT INTO users(username,password,role)
VALUES(%s,%s,%s)
""",(username,hashed,"Admin"))

conn.commit()

print("Admin Created")
