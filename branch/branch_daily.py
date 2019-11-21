from datetime import datetime, timedelta, date

import argparse
import dateutil.parser  # pip install python-dateutil

from dateparser import dateparser
from DatadogMetric import get_metric, DatadogDetail

from json2csv import list_from_json, write_csv

yesterday = datetime.now() - timedelta(hours=2)
# yesterday = yesterday.strftime('%Y-%m-%d')
yesterday = yesterday.strftime('%Y-%m-%d %H:00:00')
today = datetime.now() - timedelta(hours=1)
# today = datetime.now() - timedelta(hours=1)
today = today.strftime('%Y-%m-%d %H:00:00')
# today = today.strftime('%Y-%m-%d')

kpi = "Disk_Used"
interval = "hourly"

parser = argparse.ArgumentParser()
parser.add_argument('-s', "--startdate", help="The Start Date - format YYYY-MM-DD", default=yesterday, required=False,
                    type=dateutil.parser.isoparse)
parser.add_argument('-e', "--enddate", help="The End Date format YYYY-MM-DD (Inclusive)", default=today, required=False,
                    type=dateutil.parser.isoparse)
parser.add_argument('-k', "--kpi", help="KPI metric ex: Disk_Used", default=kpi, required=False)
parser.add_argument('-i', "--interval", help="Interval Data, Daily / Hourly ", default=interval, required=False)

args = parser.parse_args()
argstartdate = args.startdate
argenddate = args.enddate
argkpi = args.kpi

if __name__ == '__main__':
    ### Get Start and End Date and Datadog from Argument, if not given, use default value ###

    start_date = argstartdate
    end_date = argenddate
    # print(start_date)
    # print(end_date)
    str_start_date = datetime.strftime(start_date, '%Y-%m-%d %H:00:00')
    start_date = datetime.strptime(str_start_date, '%Y-%m-%d %H:00:00')
    str_end_date = datetime.strftime(end_date, '%Y-%m-%d %H:00:00')
    end_date = datetime.strptime(str_end_date, '%Y-%m-%d %H:00:00')

    # Convert Date to datetime and epoch
    #date = dateparser.gethour(start_date, end_date)
    for single_date in daterange(start_date, end_date):
        date = dateparser.getdate(start_date, end_date)
        ystart = date[0]
        ystarttime = date[1]
        print (ystart)
        print (ystarttime)
    # yend=date[2]
    # yendtime=date[3]
    #
    # print(ystarttime)
    # print(yendtime)

    # ### Get Datadog KPI you want to extract from Argument, if not given, use default value "Disk_Used" ###
    # kpi = argkpi
    # kpi = "Nginx_Request"
    # # KPI Metric
    # metric = DatadogDetail.DDdatabase(kpi)[0]
    # # Group by Column
    # column = DatadogDetail.DDdatabase(kpi)[1]
    # # Rollup Method
    # rollup = DatadogDetail.DDdatabase(kpi)[2]
    #
    # ### Specified your group by or column ###
    # list_column = list(column.split(","))
    # # print(list_column)
    # ln_list_column = len(list_column)
    # ### Specified your group by or column ###
    #
    # # Get Metric through API #
    # # interval = "daily"
    # if interval == "daily":
    #    # Daily Metric
    #    get_metric.get_metric(ystart, yend, yesterday, column, metric, interval)
    #    # Convert Json Result to CSV #
    #    jsonfile = metric + interval + yesterday + ".json"
    # else:
    #    # Hourly Metric
    #    get_metric.get_metric(ystart, yend, yesterday, column, metric,interval)
    #    jsonfile = metric + interval + yesterday + ".json"
    #
    # data_list=list_from_json.create_list_from_json(jsonfile,list_column,ln_list_column)
    # # pathfile='/home/work/result/datadog/'
    # pathfile='.'
    # csv=write_csv.write_csv(yesterday,data_list,pathfile,metric,list_column)



