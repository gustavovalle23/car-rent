from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
from uuid import UUID


class BodyType(Enum):
    CONVERTIBLE_CAR = "Convertible Car"
    SEDAN_CAR = "Sedan Car"
    PICKUP = "Pickup"


@dataclass
class Car:
    name: str
    price: Decimal
    snow_tracks: bool
    build_year: datetime
    model_year: datetime
    body_type: BodyType
    available: bool

    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nSnow Tracks: {self.snow_tracks}\nBuild Year: {self.build_year}\nModel Year: {self.model_year}\nBody Type: {self.body_type}\nAvailable: {self.available}"

