import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3edd27bb4ba06d1ddd97fe939caf61fc'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4538'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Aykavu'
