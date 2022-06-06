import requests


def import_json():
    """
    Import data from https://github.com/gustavovalle23/car-rent/blob/master/backup/clients.json and save in database.
    """
    from database.client.repository import create_client_table

    response = requests.get('https://github.com/gustavovalle23/car-rent/blob/master/backup/clients.json')
    print(response)

