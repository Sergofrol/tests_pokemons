import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '61062a327d9ab7ca1cebbe1a66bedeb2'
HEADER = {'Countent-Type' : 'Application/json', 'trainer_token' : TOKEN}

body_creat_pokemons = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_rename = {
    "pokemon_id": "66739",
    "name": "бурозавр",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "66739"
}

'''response_creat_pokemons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creat_pokemons)
print(response_creat_pokemons.text)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

'''response_popkeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_popkeball.text)'''


