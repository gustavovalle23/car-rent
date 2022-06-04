from database.rent.repository import create_rent


def initial_seed():
    create_rent(
        car_id=1,
        client_id=1,
        initial_date='2020-01-01',
        end_date='2020-01-02',
    )
    create_rent(
        car_id=2,
        client_id=2,
        initial_date='2020-01-01',
        end_date='2020-01-02',
    )
    create_rent(
        car_id=3,
        client_id=3,
        initial_date='2020-01-01',
        end_date='2020-01-02',
    )
    create_rent(
        car_id=4,
        client_id=4,
        initial_date='2020-01-01',
        end_date='2020-01-02',
    )
    create_rent(
        car_id=5,
        client_id=5,
        initial_date='2020-01-01',
        end_date='2020-01-02',
    )
