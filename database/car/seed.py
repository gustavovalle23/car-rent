from datetime import datetime
from core.entity.car import BodyType
from database.car.repository import create_car

def initial_seed():
    create_car(
        available=True,
        build_year=datetime.today().year,
        model_year=datetime.today().year,
        name='Fiat Strada',
        price=74790/464,
        snow_tracks=False,
        body_type=BodyType.PICKUP
    )
    create_car(
        available=True,
        build_year=datetime.today().year,
        model_year=datetime.today().year,
        name='Toyota Corolla Cross',
        price=140000/464,
        snow_tracks=False,
        body_type=BodyType.SEDAN_CAR
    )
    create_car(
        available=True,
        build_year=datetime.today().year,
        model_year=datetime.today().year,
        name='Jeep Compass',
        price=135000/464,
        snow_tracks=False,
        body_type=BodyType.SEDAN_CAR
    )
