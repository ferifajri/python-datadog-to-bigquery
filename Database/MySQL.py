# You Can Use either MySQLdb or mysql.connector

# import MySQLdb   # pip install mysqlclient
# from MySQLdb import connection

import mysql.connector  ## pip install mysql-connector-python

def insertdbmysql (filename,host,username,pwd,dbname,table, ystarttime, yendtime):
   db = MySQLdb.connect(host=host, # The Host
                        user=username, # username
                        passwd=pwd, # password
                        db=dbname) # name of the data base

   cursor = db.cursor()
   Delete_First = "delete from "+mysqltable+" where date >= "+ystarttime+" and date <= "+yendtime+" "
   Query = "LOAD DATA LOCAL INFILE '"+filename+"' INTO TABLE "+table+" FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n' IGNORE 1 LINES"

   cursor.execute(Delete_First)
   cursor.execute(Query)

   db.commit()
   cursor.close()

def insertdbmysqlconnector (filename,host,username,pwd,dbname,table, ystarttime, yendtime):
   db = mysql.connector.connect(host=host, # The Host
                        user=username, # username
                        passwd=pwd, # password
                        db=dbname, allow_local_infile=True) # name of the data base

   cursor = db.cursor()
   Delete_First = "delete from "+table+" where date >= "+ystarttime+" and date <= "+yendtime+" "
   Query = "LOAD DATA LOCAL INFILE '"+filename+"' INTO TABLE "+table+" FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n' IGNORE 1 LINES"
   # print(Query)
   cursor.execute(Delete_First)
   cursor.execute(Query)

   db.commit()
   cursor.close()
