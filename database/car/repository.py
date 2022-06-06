from datetime import datetime
from typing import List, Optional


from core.entity.car import BodyType, Car
from database.common import get_cursor


def convert_to_obj(tuple_of_cars: tuple) -> List[Car]:
    cars: List[Car] = []
    for car in tuple_of_cars:
        cars.append(Car(
            id=car[0],
            name=car[1],
            price=car[2],
            snow_tracks=True if car[3] == 1 else False,
            build_year=car[4],
            model_year=car[5],
            body_type=car[6],
            available=True if car[7] == 1 else False
        ))
    return cars


def create_car_table():
    """ create car table if not exists """
    conn, c = get_cursor()
    car_attributes: str = """
    (car_id INTEGER PRIMARY KEY,
    name varchar,
    price real,
    snow_tracks boolean,
    build_year datetime,
    model_year varchar,
    body_type varchar,
    available boolean)
    """

    c.execute(f"CREATE TABLE IF NOT EXISTS cars {car_attributes}")
    conn.commit()
    conn.close()


def create_car(
        name: str,
        price: float,
        snow_tracks: bool,
        build_year: datetime,
        model_year: datetime,
        body_type: BodyType,
        available: bool = True
) -> bool:
    conn, c = get_cursor()
    c.execute("INSERT INTO cars (name, price, snow_tracks, build_year, model_year, body_type, available) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (name, price, snow_tracks, build_year, model_year, body_type.value, available))
    conn.commit()
    conn.close()
    return True


def find_car_by_name(name: str) -> list:
    conn, c = get_cursor()
    c.execute(f"SELECT * FROM cars WHERE name like '%{name}%'")
    cars = c.fetchall()
    conn.close()
    return convert_to_obj(cars)


def find_car_by_id(car_id: int) -> Optional[Car]:
    conn, c = get_cursor()
    c.execute(f"SELECT * FROM cars WHERE car_id = {car_id}")
    car = c.fetchone()
    conn.close()
    return convert_to_obj([car])


def find_cars_by_body_type(body_type: str) -> Optional[List[Car]]:
    conn, c = get_cursor()
    c.execute(f"SELECT * FROM cars WHERE body_type = '{body_type}'")
    cars: Optional[List[Car]] = c.fetchall()
    conn.close()
    return convert_to_obj(cars)


def find_all_cars() -> List[Car]:
    conn, c = get_cursor()
    c.execute("SELECT * FROM cars WHERE available = 1")
    cars = c.fetchall()
    conn.close()
    return convert_to_obj(cars)


def find_cars_between_price(price_min: float, price_max: float) -> List[Car]:
    conn, c = get_cursor()
    c.execute(
        f"SELECT * FROM cars WHERE price BETWEEN {price_min} AND {price_max}")
    cars = c.fetchall()
    conn.close()
    return convert_to_obj(cars)


def find_cars_by_year(year: datetime) -> List[Car]:
    conn, c = get_cursor()
    c.execute(f"SELECT * FROM cars WHERE build_year = '{year}'")
    cars = c.fetchall()
    conn.close()
    return convert_to_obj(cars)

def update_car(name: str, price: float, snow_tracks: bool, build_year: datetime, model_year: datetime, body_type: BodyType, available: bool, car_id: int) -> bool:
    conn, c = get_cursor()
    c.execute(f"UPDATE cars SET name = '{name}', price = {price}, snow_tracks = {snow_tracks}, build_year = '{build_year}', model_year = '{model_year}', body_type = '{body_type.value}', available = {available} WHERE car_id = {car_id}")

def import_car_from_dict(car_dict: dict) -> bool:
    conn, c = get_cursor()
    c.execute(f"INSERT INTO cars (name, price, snow_tracks, build_year, model_year, body_type, available) VALUES ('{car_dict['name']}', {car_dict['price']}, {car_dict['snow_tracks']}, '{car_dict['build_year']}', '{car_dict['model_year']}', '{car_dict['body_type']}', {car_dict['available']})")
    conn.commit()
    conn.close()
    return True
