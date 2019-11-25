from datetime import datetime, timedelta, date

import argparse
import dateutil.parser  # pip install python-dateutil

from dateparser import dateparser
# from branch import branch_daily, branch_hourly
from DatadogMetric import get_metric,DatadogDetail
from Database import DatabaseDetail, MySQL, BigQuery

from json2csv import list_from_json,write_csv

yesterday = datetime.now() - timedelta(days=1)
# yesterday = yesterday.strftime('%Y-%m-%d')
yesterday = yesterday.strftime('%Y-%m-%d %H:00:00')
today = datetime.now() - timedelta(days=0)
# today = datetime.now() - timedelta(hours=1)
today = today.strftime('%Y-%m-%d %H:00:00')
# today = today.strftime('%Y-%m-%d')

kpi="Disk_Used"
interval="daily"

parser = argparse.ArgumentParser()
parser.add_argument('-s', "--startdate",help="The Start Date - format YYYY-MM-DD",default=yesterday,required=False,type=dateutil.parser.isoparse)
parser.add_argument('-e', "--enddate",help="The End Date format YYYY-MM-DD (Inclusive)",default=today,required=False,type=dateutil.parser.isoparse)
parser.add_argument('-k', "--kpi",help="KPI metric ex: Disk_Used",default=kpi,required=False)
parser.add_argument('-i', "--interval",help="Interval Data, Daily / Hourly ",default=interval,required=False)

args = parser.parse_args()
argstartdate=args.startdate
argenddate=args.enddate
argkpi=args.kpi

if __name__ == '__main__':
   ### Get Start and End Date and Datadog from Argument, if not given, use default value ###

   start_date=argstartdate
   end_date=argenddate

   str_start_date = datetime.strftime(start_date, '%Y-%m-%d %H:00:00')
   start_date = datetime.strptime(str_start_date, '%Y-%m-%d %H:00:00')
   str_end_date = datetime.strftime(end_date, '%Y-%m-%d %H:00:00')
   end_date = datetime.strptime(str_end_date, '%Y-%m-%d %H:00:00')
   # print(start_date)
   # print(end_date)

   for single_date in dateparser.daterange(start_date, end_date):
      # print(single_date)
      # Convert Date to datetime and epoch
      date=dateparser.getdate(start_date,end_date)
      ystart=date[0]
      ystarttime=date[1]
      yend=date[2]
      yendtime=date[3]
      file_date=single_date.strftime("%Y-%m-%d")
      # file_hour=date[5]
      print(ystart)
      print(ystarttime)
      print(yend)
      print(yendtime)

      ### Get Datadog KPI you want to extract from Argument, if not given, use default value "Disk_Used" ###
      kpi = argkpi
      kpi = "Nginx_Request"
      # KPI Metric
      metric = DatadogDetail.DDdatabase(kpi)[0]
      # Group by Column
      column = DatadogDetail.DDdatabase(kpi)[1]
      # Rollup Method
      rollup = DatadogDetail.DDdatabase(kpi)[2]

      ### Specified your group by or column ###
      list_column = list(column.split(","))
      ln_list_column = len(list_column)

      #   Get Daily Metric from API
      get_metric.get_metric(ystart, yend, file_date, column, metric,interval)
      jsonfile = metric + "_" + interval + "_" + file_date + ".json"
      data_list=list_from_json.create_list_from_json(jsonfile,list_column,ln_list_column)

      # Create CSV File
      pathfile="C:\Code\Datadog\\"
      pathfile_mysql = "C:/Code/Datadog/"
      csv=write_csv.write_csv(file_date,data_list,pathfile,metric,list_column)
      filename = pathfile+metric+'_'+file_date+'.csv'
      filename_mysql = pathfile_mysql + metric + '_' + file_date + '.csv'
      # ETL to Database
      table = "dd_" + metric.replace('.', '_') + "_hourly"
      get_metric.silentremove(jsonfile)

      # MySQL Database
      host = DatabaseDetail.Database_Connection['MySQL']['host']
      username = DatabaseDetail.Database_Connection['MySQL']['username']
      pwd = DatabaseDetail.Database_Connection['MySQL']['pwd']
      dbname = DatabaseDetail.Database_Connection['MySQL']['dbname']

      MySQL.insertdbmysqlconnector(filename_mysql, host, username, pwd, dbname, table, ystarttime, yendtime)

      # BQ Database
      project_id = DatabaseDetail.Database_Connection['BigQuery']['project_id']
      dataset_id = DatabaseDetail.Database_Connection['BigQuery']['dataset_id']

      BigQuery.insertBQ(filename, project_id, dataset_id, table, ystarttime, yendtime)


