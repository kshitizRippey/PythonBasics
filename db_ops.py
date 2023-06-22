import logging
import sqlite3


def get_connection(db_name) -> sqlite3.Connection:
    return sqlite3.connect(f"{db_name}.db")


def check_if_exists(conn, username):
    query = f'SELECT username FROM user WHERE username=?'
    cursor = conn.cursor()
    result = cursor.execute(query, (username,)).fetchone()
    return True if result is not None else False


def insert_user(username, password) -> str:
    try:
        with get_connection('python_basics') as conn:
            if check_if_exists(conn, username):
                return "User already exists!"
            cursor = conn.cursor()
            query = "INSERT INTO user(username, password) VALUES (?, ?)"
            cursor.execute(query, (username, password))
            status = False
            conn.commit()
            cursor.close()
            return "User created successfully!"
    except sqlite3.DatabaseError as e:
        logging.error(str(e))
    return "Internal Server Error"


def get_stored_password(username):
    with get_connection('python_basics') as conn:
        cursor = conn.cursor()
        query = f'SELECT password FROM user WHERE username=?'
        result = cursor.execute(query, (username,)).fetchone()
        if result is not None:
            return result[0]
