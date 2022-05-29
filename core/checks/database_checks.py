from database.user.repository import get_all_users
from database.user.seed import initial_seed


def create_tables():
    from database.user.repository import create_user_table
    from database.car.repository import create_car_table

    create_user_table()
    create_car_table()


def initial_check():
    create_tables()

    users = get_all_users()
    if not users:
        initial_seed()
