import sqlite3
from database.user import create_user


def login():
    """ login with username and password """
    username = input("Username: ")
    password = input("Password: ")
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?",
              (username, password))
    user = c.fetchone()

    if not user:
        print("Invalid username or password!")
    else:
        print("Welcome!")


def register():
    """ register new user """
    name = input("Name: ")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    phone = input("Phone: ")

    create_user(name, username, password, email, phone)
    print("User registered!")
