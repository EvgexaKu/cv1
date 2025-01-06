import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7bd4a3c48d392a7b998df5bafb54c5d7'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

# Создание покемона
body_create_pokemon = {
    "name": "Слава",
    "photo_id": 1
}
response_create_pokemon = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon)
print(response_create_pokemon.json())

# Получение ID созданного покемона
PO_ID = response_create_pokemon.json()['id']

# Изменение имени покемона
body_change_pokemon = {
    "pokemon_id": PO_ID,
    "name": "Роман",
    "photo_id": 7
}
response_change_pokemon = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change_pokemon)
print(response_change_pokemon.text)

# Помещение покемона в покеболл
body_pokemon_in_pokeball = {
    "pokemon_id": PO_ID
}
response_pokemon_in_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokemon_in_pokeball)
print(response_pokemon_in_pokeball.json())