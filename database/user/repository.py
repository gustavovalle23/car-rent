import sqlite3
from typing import Optional, List

from core.entity.user import User


def create_user_table() -> None:
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


def create_user(name: str, username: str, password: str, email: str, phone: str) -> None:
    """ create new user with name, username, email and phone """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)",
              (name, username, password, email, phone))
    conn.commit()
    conn.close()


def update_user(name: str, username: str, email: str, phone: str) -> None:
    """ update user with name, username, email and phone """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, username = ?, email = ?, phone = ? WHERE username = ?",
              (name, username, email, phone, username))
    conn.commit()
    conn.close()


def get_user_by_username(username) -> Optional[User]:
    """ get user by username """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user: Optional[User] = c.fetchone()
    return user


def get_user_by_email(email) -> Optional[User]:
    """ get user by email """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user: Optional[User] = c.fetchone()
    return user


def check_if_username_exists(username: str) -> Optional[User]:
    """ check if username exists """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    return user


def check_if_password_is_correct(username: str, password: str) -> Optional[User]:
    """ check if password is correct """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?",
              (username, password))
    user: Optional[User] = c.fetchone()
    return user


def get_all_users() -> Optional[List[User]]:
    """ get all users """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users: Optional[List[User]] = c.fetchall()
    return users
