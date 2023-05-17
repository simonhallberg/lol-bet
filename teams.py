import requests
import pandas as pd 

api_key_id = 'x-api-key'
api_key_secret = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'

teams='https://esports-api.lolesports.com/persisted/gw/getTeams'
headers = {'Content-Type': 'application/json'}
auth = (api_key_id, api_key_secret)

#headers = {'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'}

response = requests.get(url=teams,auth=auth,headers=headers)
response.headers
response.request.headers

dict1=response.json()
print(dict1)
