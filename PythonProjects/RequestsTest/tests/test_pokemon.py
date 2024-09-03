import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '61062a327d9ab7ca1cebbe1a66bedeb2'
HEADER = {'Countent-Type' : 'Application/json', 'trainer_token' : TOKEN}
TREINER_ID = '5326'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TREINER_ID})
    assert response.status_code == 200