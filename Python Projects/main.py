import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOUR-TOKEN'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

new_pokemon = {
    "name": "Gavrik",
    "photo_id": 119
}

add_pokeball = {
    "pokemon_id": "45135"
}

new_name = {
    "pokemon_id": "45134",
    "name": "Klikich",
    "photo_id": 122
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = new_pokemon)
print(response.text)
message = response.json()['message']
print(message)

pokeball_response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = add_pokeball)
print(pokeball_response.text)
message_pokeball = pokeball_response.json()['message']
print(message_pokeball)

change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = new_name)
print(change_name.text)
message_name = change_name.json()['message']
print(message_name)
