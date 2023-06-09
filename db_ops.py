import sqlite3


def get_connection(db_name) -> sqlite3.Connection:
    return sqlite3.connect(f"{db_name}.db")


def insert_user(username, password) -> dict:
    try:
        with get_connection('python_basics') as conn:
            status = True
            cursor = conn.cursor()
            query = "INSERT INTO user(username, password) VALUES (?, ?)"
            try:
                cursor.execute(query, (username, password))
                status = False
                message = f"User {username} created successfully!"
                conn.commit()
            except sqlite3.IntegrityError as e:
                print(e)
                message = f"User {username} already exists!"
            finally:
                cursor.close()

            return {
                "error": status,
                "message": message
            }
    except sqlite3.DatabaseError as e:
        print(e)


def get_stored_password(username):
    with get_connection('python_basics') as conn:
        cursor = conn.cursor()
        query = f'SELECT password FROM user WHERE username=?'
        result = cursor.execute(query, (username,)).fetchone()
        if result is not None:
            return result[0]


if __name__ == '__main__':
    print(get_stored_password('testuser12'))
