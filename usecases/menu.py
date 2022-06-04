from typing import Dict, Any

from core.checks.database_checks import initial_check
from core.errors import option_not_found
from core.messages import *
from usecases.about import about
from usecases.authentication import login, register
from usecases.rent_car import rent_car

initial_choices: Dict[str, Any] = {
    "1": login,
    "2": register,
    "3": about,
    "0": exit
}


def initial_menu():
    """ show menu with login, register, logout and exit options """
    initial_check()
    print(welcome_message)
    option: str = input("\n Type your choice: ")
    initial_choices.get(option, option_not_found)()


def features_menu():
    print(features_menu_message)
    option: str = input("\n Type your choice: ")
    rent_car(option)

