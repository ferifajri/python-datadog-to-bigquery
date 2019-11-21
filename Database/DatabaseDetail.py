## Set Your Big Query / MySQL Database Connection Here

Database_Connection =  { 'MySQL': {'host': 'Your MySQl Host','username': 'Your MySQl Username','pwd':'Your MySQl Pass','dbname':'Your MySQl Database Name'},
                         'BigQuery': {'project_id':'Your BQ Project ID','dataset_id':'Your BQ Dataset ID'},
                        }

# print(Database_Connection['MySQL']['host'])
# print(Database_Connection['BigQuery']['dataset'])


def DDdatabase(kpi):
    metric = Database[kpi]['metric']
    column = Database[kpi]['column']
    rollup = Database[kpi]['rollup']
    return metric,column,rollup

