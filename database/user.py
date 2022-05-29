import sqlite3


def create_user_table():
    """
    create table if not exists user with
    name as varchar, username, password, email as varchar and phone as varchar
    """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    user_attributes: str = "(name varchar, username varchar, password varchar, email varchar, phone varchar)"
    c.execute(f"CREATE TABLE IF NOT EXISTS users {user_attributes}")
    conn.commit()
    conn.close()


def create_user(name: str, username: str, password: str, email: str, phone: str):
    """ create new user with name, username, email and phone """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)",
              (name, username, password, email, phone))
    conn.commit()
    conn.close()


def update_user(name, username, email, phone):
    """ update user with name, username, email and phone """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, username = ?, email = ?, phone = ? WHERE username = ?",
              (name, username, email, phone, username))
    conn.commit()
    conn.close()


def get_user_by_username(username):
    """ get user by username """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    return user


def get_user_by_email(email):
    """ get user by email """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = c.fetchone()
    return user


def check_if_username_exists(username: str) -> bool:
    """ check if username exists """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    if user:
        return True
    else:
        return False


def check_if_password_is_correct(username: str, password: str) -> bool:
    """ check if password is correct """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?",
              (username, password))
    user = c.fetchone()
    if user:
        return True
    else:
        return False


def get_all_users():
    """ get all users """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    return users
