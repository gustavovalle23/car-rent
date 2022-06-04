from core.common import clear_screen
from core.errors import option_not_found

from database.car.repository import *
from usecases.rent_car import rent_car


def show_cars(option: str):
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
        print(f'Options available: {" - ".join([body.value for body in BodyType])}')
        cars = find_cars_by_body_type(input("\n Enter body type: "))
    elif option == '4':
        cars = find_cars_between_price(
            input("\n Enter price min: "), input("\n Enter price max: "))
    elif option == '5':
        cars = find_cars_by_year(input("\n Enter year: "))
    else:
        option_not_found()

    if cars:
        clear_screen()
        print('Cars Found:')
        for car in cars:
            print('****************************************************')
            print(car)
        id_car = input('\n\nEnter id of car to rent (or Control C to exit): ')
        rent_car(id_car)
    else:
        print('No cars found')
