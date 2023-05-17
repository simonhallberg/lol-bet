from google.cloud import bigquery

bigquery_client = bigquery.Client(project="myproject")
dataset = bigquery_client.dataset("mydataset")

table_ref = dataset.table('my_table')
table = bigquery.Table(table_ref, schema=SCHEMA)
table = client.create_table(table)