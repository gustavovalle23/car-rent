from os import system

from core.messages import about_message


def about():
    system('clear')
    print(about_message)
