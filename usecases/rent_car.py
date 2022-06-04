from typing import Any, Dict
from core.errors import option_not_found

from database.car.repository import *


rent_choices: Dict[str, Any] = {
    "1": [find_car_by_name, ['Enter car name']],
    "2": [find_all_cars, []],
    "3": [find_cars_by_body_type, ['Enter body type']],
    "4": [find_cars_between_price, ['Enter price min', 'Enter price max']],
    "5": [find_cars_by_year, ['Enter year']],
    "0": exit
}


def rent_car(option: str):
    if option == '0':
        exit(-1)
    if option is None:
        print("\n Invalid option")

    cars: Optional[List[Car]] = None

    if option == '1':
        cars = find_car_by_name(input("\n Enter car name: "))
    elif option == '2':
        cars = find_all_cars()
    elif option == '3':
        cars = find_cars_by_body_type(input("\n Enter body type: "))
    elif option == '4':
        cars = find_cars_between_price(
            input("\n Enter price min: "), input("\n Enter price max: "))
    elif option == '5':
        cars = find_cars_by_year(input("\n Enter year: "))
    else:
        option_not_found()

    if cars:
        print('Cars Found:')
        for car in cars:
            print('****************************************************')
            print(car)
    else:
        print('No cars found')
