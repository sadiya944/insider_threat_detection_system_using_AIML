import bcrypt
from database import get_connection

def login(username, password):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT id,
               username,
               password,
               role
        FROM users
        WHERE username=%s
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if user is None:
        return False, None

    if bcrypt.checkpw(
        password.encode(),
        user["password"].encode()
    ):
        return True, user

    return False, None