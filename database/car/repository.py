import sqlite3
from datetime import datetime
from typing import List, Optional


from core.entity.car import BodyType, Car


def convert_to_obj(tuple_of_cars: tuple) -> List[Car]:
    cars: List[Car] = []
    for car in tuple_of_cars:
        cars.append(Car(
            name=car[0],
            price=car[1],
            snow_tracks=True if car[2] == 1 else False,
            build_year=car[3],
            model_year=car[4],
            body_type=car[5],
            available=True if car[6] == 1 else False
        ))
    return cars


def get_cursor():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    return conn, c


def create_car_table():
    """ create car table if not exists """
    conn, c = get_cursor()
    car_attributes: str = """
    (name varchar,
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
    c.execute("INSERT INTO cars VALUES (?, ?, ?, ?, ?, ?, ?)",
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


def find_cars_by_body_type(body_type: BodyType) -> Optional[List[Car]]:
    conn, c = get_cursor()
    c.execute(f"SELECT * FROM cars WHERE body_type = '{body_type.value}'")
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
