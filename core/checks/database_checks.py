from database.user import get_all_users
from database.utils import initial_seed


def create_tables():
    from database.user import create_user_table
    create_user_table()


def initial_check():
    create_tables()

    users = get_all_users()
    if not users:
        initial_seed()
