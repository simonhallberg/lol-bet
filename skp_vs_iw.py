import requests
import pandas as pd 

gameid='110016463799050196'
starting_time='2023-04-25T15:18:00.00Z'

champ_data_no_timestamp='https://feed.lolesports.com/livestats/v1/window/110016463799050196?startingTime=2023-04-25T15:53:00.00Z'
response = requests.get(url=champ_data_no_timestamp)
dict1=response.json()
metadata=dict1['gameMetadata']
blueteam=metadata['blueTeamMetadata']
redteam=metadata['redTeamMetadata']
blueteam_team=blueteam['esportsTeamId']
redteam_team=redteam['esportsTeamId']

blueteam_players=pd.DataFrame({"player_name":[],
                               "player_id":[]})
for i in range(5):
    new_row = {'player_name': blueteam['participantMetadata'][i]['summonerName'], 'player_id': blueteam['participantMetadata'][i]['esportsPlayerId']}
    blueteam_players.loc[len(blueteam_players)] = new_row
    
print(blueteam_players)


blueteam_champions=[None]*5
for i in range(5):
    blueteam_champions[i]=blueteam['participantMetadata'][i]['championId']
    print(i)
    print(blueteam['participantMetadata'][i]['championId'])
    
redteam_champions=[None]*5
for i in range(5):
    redteam_champions[i]=redteam['participantMetadata'][i]['championId']
    print(i)
    print(redteam['participantMetadata'][i]['championId'])
    
