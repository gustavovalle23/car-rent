from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Client:
    id: UUID
    name: str
    phone: str
    email: str
    document: str
    birth_date: datetime

    def __str__(self) -> str:
        return self.name
