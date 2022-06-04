from database.car.repository import find_all_cars
from database.user.repository import find_all_users
from database.user.seed import initial_seed as initial_seed_user
from database.car.seed import initial_seed as initial_seed_car


def create_tables():
    from database.user.repository import create_user_table
    from database.car.repository import create_car_table

    create_user_table()
    create_car_table()


def initial_check():
    create_tables()

    users = find_all_users()
    cars = find_all_cars()

    if not users:
        initial_seed_user()
    if not cars:
        initial_seed_car()
