import sqlite3
from datetime import datetime
from typing import List, Optional


from core.entity.car import BodyType


def create_car_table():
    """ create car table if not exists """
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
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
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO cars VALUES (?, ?, ?, ?, ?, ?, ?)",
              (name, price, snow_tracks, build_year, model_year, body_type.value, available))
    conn.commit()
    conn.close()
    return True


def find_car_by_name(name: str) -> list:
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM cars WHERE name = '{name}'")
    car = c.fetchall()
    conn.close()
    return car


def find_cars_by_body_type(body_type: BodyType) -> Optional[List[BodyType]]:
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM cars WHERE body_type = '{body_type.value}'")
    car: Optional[List[BodyType]] = c.fetchall()
    conn.close()
    return car
