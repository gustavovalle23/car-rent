import os


def clear_screen():
    """ clear screen if user in linux and windows """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
