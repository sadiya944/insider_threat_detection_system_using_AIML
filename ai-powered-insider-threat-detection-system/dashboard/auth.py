import bcrypt
from database import get_connection

def login(username, password):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    "SELECT * FROM users WHERE username=?",
    (username,)
)

   row = cursor.fetchone()

if row:
    user = dict(row)

    conn.close()

    if user is None:
        return False, None

    if bcrypt.checkpw(
        password.encode(),
        user["password"].encode()
    ):
        return True, user

    return False, None
