from dataclasses import dataclass
from core.entity.car import Car
from core.entity.client import Client
from uuid import UUID


@dataclass
class Rent:
    id: UUID
    car_id: int
    initial_date: str
    end_date: str
    client_id: int

    def __str__(self) -> str:
        return f'{self.car.name} - {self.client.name}'
