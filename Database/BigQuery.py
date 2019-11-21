from credentials import BigQuery
BQCredential = BigQuery.BQ_json()

### BQ Credential ###
import os
# pip install --upgrade google-cloud-bigquery
from google.cloud import bigquery
from google.cloud.bigquery import Client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = BQCredential
os.environ['GOOGLE_CLOUD_DISABLE_GRPC'] = 'True'
client = bigquery.Client()
###




# ### BQ Credential ###
# from google.cloud import bigquery
# from google.cloud.bigquery import Client
# from google.oauth2 import service_account
#
# key_path= '/home/work/GCP/billing-production-infra-29ba-02abdd9608dc.json'
#
# SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/bigquery']
# SERVICE_ACCOUNT_FILE = '/home/work/GCP/billing-production-infra-29ba-02abdd9608dc.json'
#
# credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#
# delegated_credentials = credentials.with_subject('csv-import@billing-production-infra-29ba.iam.gserviceaccount.com')
# project = "billing-production-infra-29ba"
# client = bigquery.Client(credentials=delegated_credentials, project=project)
#
# ###

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

