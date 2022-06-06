from typing import Optional, List

from core.entity.user import User
from database.common import get_cursor


def convert_to_obj(tuple_of_users: tuple) -> List[User]:
    if not tuple_of_users:
        return
    if not tuple_of_users[0]:
        return

    users: List[User] = []
    for user in tuple_of_users:
        users.append(User(
            id=str(user[0]),
            name=user[1],
            username=user[2],
            password=user[3],
            email=user[4],
            phone=user[5]
        ))
    return users


def create_user_table() -> None:
    """
    create table if not exists user with
    name as varchar, username, password, email as varchar and phone as varchar
    """
    conn, c = get_cursor()
    user_attributes: str = "(user_id INTEGER PRIMARY KEY, name varchar, username varchar, password varchar, email varchar, phone varchar)"
    c.execute(f"CREATE TABLE IF NOT EXISTS users {user_attributes}")
    conn.commit()
    conn.close()


def create_user(name: str, username: str, password: str, email: str, phone: str) -> None:
    """ create new user with name, username, email and phone """
    conn, c = get_cursor()
    c.execute("INSERT INTO users(name, username, password, email, phone) VALUES (?, ?, ?, ?, ?)",
              (name, username, password, email, phone))
    conn.commit()
    conn.close()


def update_user(name: str, username: str, email: str, phone: str) -> None:
    """ update user with name, username, email and phone """
    conn, c = get_cursor()
    c.execute("UPDATE users SET name = ?, username = ?, email = ?, phone = ? WHERE username = ?",
              (name, username, email, phone, username))
    conn.commit()
    conn.close()


def find_user_by_username(username) -> Optional[User]:
    """ get user by username """
    conn, c = get_cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user: Optional[User] = c.fetchone()
    conn.close()
    return convert_to_obj([user])


def find_user_by_email(email) -> Optional[User]:
    """ get user by email """
    conn, c = get_cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user: Optional[User] = c.fetchone()
    conn.close()
    return convert_to_obj([user])


def check_if_username_exists(username: str) -> Optional[User]:
    """ check if username exists """
    conn, c = get_cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    return convert_to_obj([user])


def check_if_password_is_correct(username: str, password: str) -> Optional[User]:
    """ check if password is correct """
    conn, c = get_cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?",
              (username, password))
    user: Optional[User] = c.fetchone()
    conn.close()
    return convert_to_obj([user])


def find_all_users() -> Optional[List[User]]:
    """ get all users """
    conn, c = get_cursor()
    c.execute("SELECT * FROM users")
    users: Optional[List[User]] = c.fetchall()
    conn.close()
    return convert_to_obj(users)

def import_user_from_dict(user_dict: dict) -> None:
    """ import user from dict """
    create_user(user_dict["name"], user_dict["username"], user_dict["password"], user_dict["email"], user_dict["phone"])
