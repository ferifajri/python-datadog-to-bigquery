import json
import datetime as dtime

def create_list_from_json(jsonfile,list_column,ln_list_column):

    with open(jsonfile) as f:
        data = json.load(f)
#    pprint(data)

    data_list = []  # create an empty list
    for x in range(0,(len(data['series'])),1):
        for i in range (0,len(data['series'][0]['pointlist']),1):
            # append the items to the list in the same order.
            scope = data['series'][x]['scope']
            scope = scope.split(',')

            dates = data['series'][x]['pointlist'][i][0]
            dates = str(dates)[:10]
            dates = float(dates)
            # print(dates)
            date = dtime.datetime.utcfromtimestamp(dates)
            # print(date)
            date = str(date)


            value = data['series'][x]['pointlist'][i][1]
            value= str(value)

            mycolumnlist=[]
            for c in range(0,ln_list_column):
                # appindex = [idx for idx, s in enumerate(scope) if 'app:' in s][0]
                # app = scope[appindex]
                # app = app[4:len(app)]
                mycolumn=list_column[int(c)]
                mycolumnindex=[idx for idx, s in enumerate(scope) if mycolumn+':' in s][0]
                # print(mycolumnindex)
                mycolumn=scope[mycolumnindex]
                mycolumn=mycolumn[0:len(mycolumn)]
                mycolumn=mycolumn.split(':')[1]
                if mycolumn == 'N/A':
                    mycolumn=""

                # print(mycolumn)

                mycolumnlist.append(mycolumn)
            # print(mycolumn)
            data_column=""
            for element in mycolumnlist:
                data_column += element+","
            data_list.append(date+","+data_column+value)
            # data_list.append(date + ';' + env + ';' + service + ';' + app + ';' + role + ';' + cluster + ';' + tribe + ';' + squad + ';' + host + ';' + value)

#env,tribe,squad,service,app,cluster,role,host
             # data_list.append(date+';'+env+';'+service+';'+app+';'+role+';'+cluster+';'+tribe+';'+squad+';'+host+';'+value)
    return data_list
#    print(data_list)

# column = "env,tribe,squad,service,app,cluster,role,host"
# print (column)
# list_column = list(column.split(","))
# print(list_column[0])
# ln_list_column = len(list_column)
# print(ln_list_column)
# jsonfile="../nginx.net.request_per_s_daily_2019-11-13.json"
# data_list=create_list_from_json(jsonfile,list_column,ln_list_column)
# print(data_list)
