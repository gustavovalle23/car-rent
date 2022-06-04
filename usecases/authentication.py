from typing import Optional
from core.entity.user import User

from database.user.repository import check_if_password_is_correct, create_user


def login():
    from usecases.menu import features_menu
    """ login with username and password """
    username = input("Username: ")
    password = input("Password: ")

    user: Optional[User] = check_if_password_is_correct(username, password)

    if not user:
        print("Invalid username or password!")
    else:
        print("Welcome!")
        features_menu()


def register():
    """ register new user """
    name = input("Name: ")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    phone = input("Phone: ")

    create_user(name, username, password, email, phone)
    print("User registered!")
