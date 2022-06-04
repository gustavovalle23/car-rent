from typing import List
from database.common import get_cursor
from core.entity.rent import Rent


def convert_to_obj(tuple_of_rents: tuple) -> List[Rent]:
    if not tuple_of_rents:
        return
    if not tuple_of_rents[0]:
        return

    rents: List[Rent] = []
    for rent in tuple_of_rents:
        rents.append(Rent(
            id=str(rent[0]),
            car_id=str(rent[1]),
            client_id=str(rent[2]),
            initial_date=rent[3],
            end_date=rent[4],
        ))
    return rents


def create_rent_table():
    """ create rent table if not exists """
    conn, c = get_cursor()
    rent_attributes: str = """
    (rent_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    client_id INTEGER,
    initial_date datetime,
    end_date datetime,
    FOREIGN KEY (car_id) REFERENCES cars(car_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id))
    """

    c.execute(f"CREATE TABLE IF NOT EXISTS rents {rent_attributes}")
    conn.commit()
    conn.close()


def find_all_rents() -> List[Rent]:
    conn, c = get_cursor()
    c.execute("SELECT * FROM rents")
    rents = c.fetchall()
    conn.close()
    return convert_to_obj(rents)


def find_rent_by_id(rent_id: str) -> Rent:
    conn, c = get_cursor()
    c.execute(f"SELECT * FROM rents WHERE rent_id = {rent_id}")
    rent = c.fetchone()
    conn.close()
    return convert_to_obj(rent)


def create_rent(car_id: str, client_id: str, initial_date: str, end_date: str) -> None:
    conn, c = get_cursor()
    c.execute("INSERT INTO rents(car_id, client_id, initial_date, end_date) VALUES (?, ?, ?, ?)",
              (car_id, client_id, initial_date, end_date))
    conn.commit()
    conn.close()


def update_rent(rent_id: str, car_id: str, client_id: str, initial_date: str, end_date: str) -> None:
    conn, c = get_cursor()
    c.execute("UPDATE rents SET car_id = ?, client_id = ?, initial_date = ?, end_date = ? WHERE rent_id = ?",
              (car_id, client_id, initial_date, end_date, rent_id))
    conn.commit()
    conn.close()


def delete_rent(rent_id: str) -> None:
    conn, c = get_cursor()
    c.execute(f"DELETE FROM rents WHERE rent_id = {rent_id}")
    conn.commit()
    conn.close()


def find_rents_by_client_id(client_id: str) -> List[Rent]:
    conn, c = get_cursor()
    c.execute(f"SELECT * FROM rents WHERE client_id = {client_id}")
    rents = c.fetchall()
    conn.close()
    return convert_to_obj(rents)


def find_rents_by_car_id(car_id: str) -> List[Rent]:
    conn, c = get_cursor()
    c.execute(f"SELECT * FROM rents WHERE car_id = {car_id}")
    rents = c.fetchall()
    conn.close()
    return convert_to_obj(rents)


def find_rents_by_initial_date(initial_date: str) -> List[Rent]:
    conn, c = get_cursor()
    c.execute(f"SELECT * FROM rents WHERE initial_date = '{initial_date}'")
    rents = c.fetchall()
    conn.close()
    return convert_to_obj(rents)


def find_rents_by_end_date(end_date: str) -> List[Rent]:
    conn, c = get_cursor()
    c.execute(f"SELECT * FROM rents WHERE end_date = '{end_date}'")
    rents = c.fetchall()
    conn.close()
    return convert_to_obj(rents)
