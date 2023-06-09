import requests
import pandas as pd

api_key = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
hl='en-US'
teams_url = 'https://esports-api.lolesports.com/persisted/gw/getTeams?hl='+hl

headers = {'Content-Type': 'application/json', 'x-api-key': api_key}

response = requests.get(url=teams_url, headers=headers)
dict=response.json()

teams=dict['data']['teams']

all_teams=pd.DataFrame({"id":[],
                        "name":[],
                        "row_num":[]})
for i in range(len(teams)):
    new_row = {'id': teams[i]['id'], 'name': teams[i]['name'], 'row_num': i}
    all_teams.loc[len(all_teams)] = new_row

#print(all_teams)

g2_row = all_teams.loc[all_teams['name'] == 'G2 Esports']

g2_row_num = all_teams.loc[all_teams['name'] == 'G2 Esports']['row_num'].values[0]



#print(type(teams))
g2=teams[g2_row_num]
print(teams)
print(g2)

df = pd.read_csv('2023_LoL_esports_match_data_from_OraclesElixir.csv')

g2 = df[df['teamname'] == g2['name']]


blueteam=metadata['blueTeamMetadata']
redteam=metadata['redTeamMetadata']
blueteam_team=blueteam['esportsTeamId']
redteam_team=redteam['esportsTeamId']
