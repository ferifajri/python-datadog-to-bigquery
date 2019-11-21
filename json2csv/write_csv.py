import pandas as pd
# if you have some difficulty installing pandas package and using python 3, try to downgrade your setup tools
# pip uninstall setuptools
# pip install setuptools==39.1.0
# https://github.com/googleapis/google-cloud-python/issues/2990#issuecomment-502986564
import csv

def write_csv_hourly(file_date,file_hour,data_list,pathfile,metric,list_column):

    df = pd.DataFrame(data=data_list)

    # with open('/home/work/result/datadog/nginx.net.request_per_s_'+yesterday+'.csv', 'w',newline='') as c:
    with open(''+pathfile+metric+'_'+file_date+'_'+file_hour+'.csv', 'w', newline='') as c:
        list_column_csv = ""
        for lc in list_column:
            list_column_csv += lc+";"
            # list_column_csv += """+lc"""+","
        # Add Header
        writer = csv.writer(c)
        writer.writerow(["date;"+list_column_csv+"value"])

        for item in data_list: # data_list from json file
            # Set Your Column Delimiter here
            column = item.replace(',',';')
            # print(column)
            c.write("%s\n" % column)
    c.close()

def write_csv(file_date,data_list,pathfile,metric,list_column):

    df = pd.DataFrame(data=data_list)

    # with open('/home/work/result/datadog/nginx.net.request_per_s_'+yesterday+'.csv', 'w',newline='') as c:
    with open(''+pathfile+metric+'_'+file_date+'.csv', 'w', newline='') as c:
        list_column_csv = ""
        for lc in list_column:
            list_column_csv += lc+";"

        # Add Header
        writer = csv.writer(c)
        writer.writerow(["date;" + list_column_csv + "value"])

        for item in data_list: # data_list from json file
            # print(item)
            # Set Your Column Delimiter here
            column = item.replace(',',';')
            c.write("%s\n" % column)
    c.close()