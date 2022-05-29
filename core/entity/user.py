from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: UUID
    name: str
    username: str
    password: str
    email: str
    phone: str
