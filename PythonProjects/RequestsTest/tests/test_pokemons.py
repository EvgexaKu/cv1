import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7bd4a3c48d392a7b998df5bafb54c5d7'
TRAINER_ID = '12941'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}



def test_status_code():
    response = requests.get(url=f'{URL}/trainers', headers=HEADER)
    assert response.status_code == 200
 
'''def test_trainer_name_in_response():
    trainer_id = 'TRAINER_ID'
    response = requests.get(f'{URL}/trainers/trainers?trainer_id={trainer_id}')
    assert 'EvgexaK' 
    print(response.text)'''

def test_piece_body():
    response = requests.get(
        'https://api.pokemonbattle.ru/v2/trainers',
        params={'trainer_name': 'EvgexaK', 'trainer_id': TRAINER_ID},
         )
    assert response.json()["data"][0]["trainer_name"] == "EvgexaK"
   



