import requests

URL = 'https://api.pokemonbattle.me/v2'
Token = 'Token'

Headers = {'Content-Type': 'application/json', 'trainer_token': Token}

Body = {
    "name": "Кёльн",
    "photo": "https://dolnikov.ru/pokemons/albums/025.png"
}

response = requests.post(url=f'{URL}/pokemons', headers=Headers, json=Body)

print(response.text)

import requests

URL = 'https://api.pokemonbattle.me/v2'
Token = 'Token'
id = '14253'

Headers = {'Content-Type': 'application/json', 'trainer_token': Token}

Body = {
    "pokemon_id": id,
    "name": "Скуффи",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response = requests.put(url=f'{URL}/pokemons', headers=Headers, json=Body)

print(response.text)

import requests

URL = 'https://api.pokemonbattle.me/v2'
Token = 'token'

Headers = {'Content-Type': 'application/json', 'trainer_token': Token}
id = '14253'
Body = {'pokemon_id': id}

response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=Headers, json=Body)

print(response.text)


