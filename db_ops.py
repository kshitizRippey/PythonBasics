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
