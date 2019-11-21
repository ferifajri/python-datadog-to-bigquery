from credentials import datadog
from datadog import initialize, api
from json import dump

api_key = datadog.datadog_api()[0]
app_key = datadog.datadog_api()[1]

def get_metric(ystart,yend,file_date,column,metric,interval):
   options = {'api_key': api_key,'app_key': app_key}

   initialize(**options)

   #query = 'max:nginx.net.request_per_s{*}by{env,tribe,squad,service,app,cluster,role,host}.rollup(avg, 86400)'
   query = "max:"+metric+"{*}by{"+column+"}.rollup(max, 3600)"
   #query = 'query'
   #print(query)
   results = api.Metric.query(start=ystart, end=yend, query=query)
   #print(results)
   with open(metric+"_"+interval+"_"+file_date+".json", "w") as f:
     dump(results, f)

def get_metric_hourly(ystart,yend,file_date,file_hour,column,metric,interval):
   options = {'api_key': api_key,'app_key': app_key}

   initialize(**options)

   #query = 'max:nginx.net.request_per_s{*}by{env,tribe,squad,service,app,cluster,role,host}.rollup(avg, 86400)'
   query = "max:"+metric+"{*}by{"+column+"}.rollup(max, 3600)"
   #query = 'query'
   # print(query)
   results = api.Metric.query(start=ystart, end=yend, query=query)
   # print(results)
   with open(metric+"_"+interval+"_"+file_date+"_"+file_hour+".json", "w") as f:
   #with open("test.json", "w") as f:
     dump(results, f)