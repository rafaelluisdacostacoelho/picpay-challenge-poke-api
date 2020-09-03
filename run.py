import pandas
import requests

from datetime import date

response = requests.get('https://pogoapi.net/api/v1/fast_moves.json')

today = date.today().strftime('%d/%m/%Y')

dataframe = pandas.json_normalize(response.json())

dataframe['id'] = dataframe.index + 1
dataframe['total_damage'] = dataframe.power * dataframe.duration
dataframe['created_at'] = today

dataframe = dataframe[['id',
                       'stamina_loss_scaler',
                       'name',
                       'power',
                       'duration',
                       'energy_delta',
                       'type',
                       'total_damage',
                       'created_at',
                       'move_id']]

del dataframe['move_id']

dataframe.to_csv('pokemon.csv', encoding='utf-8', index=False)
