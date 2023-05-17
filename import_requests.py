import requests
import pandas as pd

gameid='110016463799050196'
starting_time='2023-04-25T15:53:00.00Z'

teams='https://esports-api.lolesports.com/persisted/gw/getTeams'

champ_data_no_timestamp='https://feed.lolesports.com/livestats/v1/window/'+gameid+'?startingTime='+starting_time

#api_url = "https://jsonplaceholder.typicode.com/todos/1"
api_url = "https://feed.lolesports.com/livestats/v1/details/107417059263365738?startingTime=2022-01-29T16:10:00.00Z"
response = requests.get(api_url)
dict1=response.json()
print(type(dict1))
df=pd.DataFrame.from_dict(dict1)
print(type(df))
#print(df)
a=df.iloc[1]
print(a)
b=a[0]
c=b['participants']


test=dict1['frames']
test2=test[0]
test3=test2['participants']
test4=test3[0]
test5=test4['abilities']

testB=test[20]


champ_data = 'https://feed.lolesports.com/livestats/v1/window/107417059263365738?startingTime=2022-01-29T16:10:00.00Z'
response = requests.get(champ_data)
dict2=response.json()
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
    
champ_data_no_timestamp='https://feed.lolesports.com/livestats/v1/window/107566458490383650?startingTime=2022-01-22T15:15:00.00Z'
response = requests.get(champ_data_no_timestamp)
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
    
