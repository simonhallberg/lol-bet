import pandas as pd
import numpy as np
from google.cloud import bigquery
import os, json

import requests

api_key = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
hl='en-US'
teams_url = 'https://esports-api.lolesports.com/persisted/gw/getTeams?hl='+hl

headers = {'Content-Type': 'application/json', 'x-api-key': api_key}

response = requests.get(url=teams_url, headers=headers)
dict=response.json()

### Converts schema dictionary to BigQuery's expected format for job_config.schema
def format_schema(schema):
    formatted_schema = []
    for row in schema:
        formatted_schema.append(bigquery.SchemaField(row['name'], row['type'], row['mode']))
    return formatted_schema

### Create dummy data to load
df = pd.DataFrame([[2, 'Jane', 'Doe']],
columns=['id', 'first_name', 'last_name'])

### Convert dataframe to JSON object
json_data = df.to_json(orient = 'records')
json_object = json.loads(json_data)
#json_object = dict

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/home/simon/lol_api/lol-bet-4a5208fe18db.json"

### Define schema as on BigQuery table, i.e. the fields id, first_name and last_name   
table_schema = {
          'name': 'id',
          'type': 'INTEGER',
          'mode': 'REQUIRED'
          }, {
          'name': 'first_name',
          'type': 'STRING',
          'mode': 'NULLABLE'
          }, {
          'name': 'last_name',
          'type': 'STRING',
          'mode': 'NULLABLE'
          }

project_id = 'lol-bet'
dataset_id = 'teams'
table_id = 'test_json_to_bq2'

client  = bigquery.Client(project = project_id)
dataset  = client.dataset(dataset_id)
table = dataset.table(table_id)

job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
job_config.schema = format_schema(table_schema)
job = client.load_table_from_json(json_object, table, job_config = job_config)

print(job.result())