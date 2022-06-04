from database.car.repository import find_all_cars
from database.client.repository import create_client_table, find_all_clients
from database.rent.repository import create_rent_table, find_all_rents
from database.user.repository import find_all_users
from database.user.seed import initial_seed as initial_seed_user
from database.car.seed import initial_seed as initial_seed_car
from database.client.seed import initial_seed as initial_seed_client
from database.rent.seed import initial_seed as initial_seed_rent


def create_tables():
    from database.user.repository import create_user_table
    from database.car.repository import create_car_table

    create_user_table()
    create_car_table()
    create_client_table()
    create_rent_table()


def initial_check():
    create_tables()

    users = find_all_users()
    cars = find_all_cars()
    clients = find_all_clients()
    rents = find_all_rents()

    if not users:
        initial_seed_user()
    if not cars:
        initial_seed_car()
    if not clients:
        initial_seed_client()
    if not rents:
        initial_seed_rent()
