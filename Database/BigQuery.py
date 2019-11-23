from credentials import BigQuery
BQ_Credential = BigQuery.BQ_json()[0]
BQ_ServiceAccount = BigQuery.BQ_json()[1]
BQ_ProjectID = BigQuery.BQ_json()[2]

# ### BQ Credential ###
import os
from google.cloud import bigquery
from google.cloud.bigquery import Client
from google.oauth2 import service_account

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = BQ_Credential
os.environ['GOOGLE_CLOUD_DISABLE_GRPC'] = 'True'

SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/bigquery']
SERVICE_ACCOUNT_FILE = BQ_Credential

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

delegated_credentials = credentials.with_subject(BQ_ServiceAccount)
project_id = BQ_ProjectID
client = bigquery.Client(credentials=delegated_credentials, project=project_id)

###

from Database import DatabaseDetail

def BQdatabase(kpi):
    metric = Database[kpi]['metric']
    column = Database[kpi]['column']
    rollup = Database[kpi]['rollup']
    return metric,column,rollup

def insertBQ(filename,project_id,dataset_id,table,ystarttime, yendtime):
   dataset_ref = client.dataset(dataset_id)
   table_ref = dataset_ref.table(table)

   query_sql = "Delete FROM `"+project_id+"."+dataset_id+"."+table+"` WHERE date >="+ystarttime+" and date <= "+yendtime+";"
   # print(query_sql)
   query_job = client.query(
       query_sql)
   query_job.result()  # Waits for the query to finish
   print('Delete Old Record from table `{}.{}.{}`'.format(project_id,dataset_id,table))

   job_config = bigquery.LoadJobConfig()

   job_config.source_format = bigquery.SourceFormat.CSV
   job_config.skip_leading_rows = 1
   job_config.autodetect = True
   job_config.field_delimiter = ';'
   job_config.encoding = "UTF-8"

   with open(filename, "rb") as source_file:
       # print(source_file)
       job = client.load_table_from_file(
           source_file,
           table_ref,
           location="US",  # Must match the destination dataset location.
           job_config=job_config)  # API request

   job.result()  # Waits for table load to complete.

   print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table))
