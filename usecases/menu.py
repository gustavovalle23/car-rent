from typing import Dict, Any

from core.checks.database_checks import initial_check
from core.messages import welcome_message
from usecases.about import about
from usecases.authentication import login, register
from core.errors import option_not_found

choices: Dict[str, Any] = {
    "1": login,
    "2": register,
    "3": about,
    "0": 'exit_app'
}


def menu():
    """ show menu with login, register, logout and exit options """
    initial_check()
    print(welcome_message)
    option: str = input("\n Type your choice: ")
    action = choices.get(option, option_not_found)
    action()
