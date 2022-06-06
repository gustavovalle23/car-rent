from datetime import datetime
from typing import List, Optional

from database.common import get_cursor
from core.entity.client import Client


def convert_to_obj(tuple_of_clients: tuple) -> List[Client]:
    if not tuple_of_clients:
        return
    if not tuple_of_clients[0]:
        return

    clients: List[Client] = []
    for client in tuple_of_clients:
        clients.append(Client(
            id=str(client[0]),
            name=str(client[1]),
            phone=str(client[2]),
            email=client[3],
            document=client[4],
            birth_date=client[5]
        ))
    return clients

def create_client_table():
    conn, c = get_cursor()
    client_attributes = """ 
    CREATE TABLE IF NOT EXISTS clients(client_id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, document TEXT, birth_date TEXT)
    """
    c.execute(client_attributes)
    conn.commit()
    conn.close()


def create_client(name: str, email: str, phone: str, document: str, birth_date: datetime) -> None:
    conn, c = get_cursor()
    c.execute("INSERT INTO clients(name, email, phone, document, birth_date) VALUES (?, ?, ?, ?, ?)",
              (name, email, phone, document, str(birth_date)))
    conn.commit()
    conn.close()


def find_client_by_name(name: str) -> Optional[Client]:
    conn, c = get_cursor()
    c.execute("SELECT * FROM clients WHERE name = ?", (name,))
    client: Optional[Client] = c.fetchone()
    conn.close()
    return convert_to_obj([client])


def find_all_clients() -> Optional[List[Client]]:
    conn, c = get_cursor()
    c.execute("SELECT * FROM clients")
    clients: list = c.fetchall()
    conn.close()
    return convert_to_obj(clients)


def update_client(id: str, name: str, email: str, phone: str, document: str, birth_date: datetime) -> None:
    conn, c = get_cursor()
    c.execute("UPDATE clients SET name = ?, email = ?, phone = ?, document = ?, birth_date = ? WHERE client_id = ?",
              (name, email, phone, document, str(birth_date), id))
    conn.commit()
    conn.close()


def delete_client(name: str) -> None:
    conn, c = get_cursor()
    c.execute("DELETE FROM clients WHERE name = ?", (name,))
    conn.commit()
    conn.close()


def delete_all_clients() -> None:
    conn, c = get_cursor()
    c.execute("DELETE FROM clients")
    conn.commit()
    conn.close()


def check_if_client_exists(name: str) -> Optional[Client]:
    conn, c = get_cursor()
    c.execute("SELECT * FROM clients WHERE name = ?", (name,))
    client: Optional[Client] = c.fetchone()
    conn.close()
    return convert_to_obj([client])


def find_client_by_email(email: str) -> Optional[Client]:
    conn, c = get_cursor()
    c.execute("SELECT * FROM clients WHERE email = ?", (email,))
    client: Optional[Client] = c.fetchone()
    conn.close()
    return convert_to_obj([client])


def find_client_by_phone(phone: str) -> Optional[Client]:
    conn, c = get_cursor()
    c.execute("SELECT * FROM clients WHERE phone = ?", (phone,))
    client: Optional[Client] = c.fetchone()
    conn.close()
    return convert_to_obj([client])


def find_client_by_id(id: str) -> Optional[Client]:
    conn, c = get_cursor()
    c.execute("SELECT * FROM clients WHERE client_id = ?", (id,))
    client: Optional[Client] = c.fetchone()
    conn.close()
    return convert_to_obj([client])


def find_client_by_document(document: str) -> Optional[Client]:
    conn, c = get_cursor()
    c.execute("SELECT * FROM clients WHERE document = ?", (document,))
    client: Optional[Client] = c.fetchone()
    conn.close()
    return convert_to_obj([client])

def import_client_from_dict(client_dict: dict) -> None:
    create_client(
        name=client_dict['name'],
        email=client_dict['email'],
        phone=client_dict['phone'],
        document=client_dict['document'],
        birth_date=client_dict['birth_date']
    )
