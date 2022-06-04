from database.client.repository import create_client


def initial_seed():
    create_client(
        name='John Doe',
        email='john@gmail.com',
        phone='+5511999999999',
        birth_date='2020-01-01',
        document='123456789'
    )
    create_client(
        name='Maria João',
        email='maria@gmail.com',
        phone='+5511999999999',
        birth_date='2020-01-01',
        document='123456786'
    )
    create_client(
        name='Maria João 2',
        email='maria@gmail.com',
        phone='+5511999999999',
        birth_date='2020-01-01',
        document='123456787'
    )
    create_client(
        name='Maria João 3',
        email='maria@gmail.com',
        phone='+5511999999999',
        birth_date='2020-01-01',
        document='123456788'
    )
    create_client(
        name='Maria João 4',
        email='maria@gmail.com',
        phone='+5511999999999',
        birth_date='2020-01-01',
        document='123456780'
    )
