### Setup Here First
# Define Your Metric on this Dictionary
Database =  { 'Disk_Used':   {'metric': 'system.disk.used','column': 'cluster,role,host','rollup':'max'},
              'Memory_Used':   {'metric': 'memory.disk.used','column': 'cluster,role,host','rollup':'max'},
              'Nginx_Request':   {'metric': 'nginx.net.request_per_s','column': 'cluster,role,host','rollup':'max'}}

# kpi="Disk_Used"
def DDdatabase(kpi):
    metric=Database[kpi]['metric']
    column = Database[kpi]['column']
    rollup = Database[kpi]['rollup']
    # table = Database[kpi]['table']
    return metric,column,rollup

