from google.cloud import storage
import json

import requests

api_key = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
hl='en-US'
teams_url = 'https://esports-api.lolesports.com/persisted/gw/getTeams?hl='+hl

headers = {'Content-Type': 'application/json', 'x-api-key': api_key}

response = requests.get(url=teams_url, headers=headers)
dict=response.json()
teams=dict['data']['teams']

result = {}
for d in teams:
    result.update(d)
 
print(result)


json_object = json.dumps(result)
type(json_object)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

# credentials to get access google cloud storage
# write your key path in place of gcloud_private_key.json
storage_client = storage.Client.from_service_account_json('lol-bet-4a5208fe18db.json')

# write your bucket name in place of bucket1go
bucket_name = 'lol-bet-bucket'
BUCKET = storage_client.get_bucket(bucket_name)

def create_json(json_object, filename):
    '''
    this function will create json object in
    google cloud storage
    '''
    # create a blob
    blob = BUCKET.blob(filename)
    # upload the blob 
    blob.upload_from_string(
        data=json.dumps(json_object),
        content_type='application/json'
        )
    result = filename + ' upload complete'
    return {'response' : result}

# your object
json_object = teams
# set the filename of your json object
filename = 'teams.json'

# run the function and pass the json_object
print(create_json(json_object, filename))