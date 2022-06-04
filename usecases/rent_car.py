from core.common import clear_screen
from core.errors import option_not_found

from database.car.repository import *
from database.client.repository import find_all_clients
from database.rent.repository import create_rent, find_all_rents


def rent_car(option: str):
    if option == '0':
        exit(-1)
    if option is None:
        print("\n Invalid option")

    cars: Optional[List[Car]] = None

    clear_screen()
    if option == '1':
        cars = find_car_by_name(input("\n Enter car name: "))
    elif option == '2':
        cars = find_all_cars()
    elif option == '3':
        print(
            f'Options available: {" - ".join([body.value for body in BodyType])}')
        cars = find_cars_by_body_type(input("\n Enter body type: "))
    elif option == '4':
        cars = find_cars_between_price(
            input("\n Enter price min: "), input("\n Enter price max: "))
    elif option == '5':
        cars = find_cars_by_year(input("\n Enter year: "))
    elif option == '6':
        print(find_all_rents())
    elif option == '7':
        print(find_all_clients())
    elif option == '8':
        create_car(
            input("\n Enter car name: "),
            float(input("\n Enter car price: ")),
            True if input(
                "\n Enter car snow tracks (True/False): ") == 'True' else False,
            datetime.strptime(
                input("\n Enter car build year (YYYY-MM-DD): "), "%Y-%m-%d"),
            input("\n Enter car model year (YYYY-MM-DD): "),
            BodyType(input("\n Enter car body type: ")),
            True if input(
                "\n Enter car available: (True/False): ") == 'True' else False
        )
        print('\n Car created')
    elif option == '9':
        id_car = input("\n Enter car id: ")
        car = find_car_by_id(id_car)
        if not car:
            print(f'Car with id {id_car} not found')
            exit(-1)
        car = car[0]

        update_car(
            car_id=id_car,
            name=input(f"\n Enter car name: {car.name}: "),
            price=float(input(f"\n Enter car price: {car.price}: ")),
            snow_tracks=True if input(
                f"\n Enter car snow tracks (True/False): {car.snow_tracks}: ") == 'True' else False,
            build_year=datetime.strptime(
                input(f"\n Enter car build year (YYYY-MM-DD): {car.build_year}: "), "%Y-%m-%d"),
            model_year=input(
                f"\n Enter car model year (YYYY-MM-DD): {car.model_year}: "),
            body_type=BodyType(
                input(f"\n Enter car body type: {car.body_type}: ")),
            available=True if input(
                f"\n Enter car available: (True/False): {car.available}: ") == 'True' else False
        )
        print('\n Car updated')
    else:
        option_not_found()

    if cars:
        clear_screen()
        print('Cars Found:')
        for car in cars:
            print('****************************************************')
            print(car)
        id_car = input('\n\nEnter id of car to rent (or Control C to exit): ')
        clients = find_all_clients()
        for client in clients:
            print(f'{client.id} - {client.name}')
        select_client = input(f'\n\nEnter id of client: ')
        choosed_car = find_car_by_id(id_car)
        start_date_of_rent = input('\n\nEnter start date of rent: ')
        end_date_of_rent = input('\n\nEnter end date of rent: ')
        create_rent(choosed_car[0].id, select_client,
                    start_date_of_rent, end_date_of_rent)
        print('\n\nRent created')
