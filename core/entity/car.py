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
    id: UUID
    name: str
    price: Decimal
    snow_tracks: bool
    build_year: datetime
    model_year: datetime
    body_type: BodyType
    available: bool

