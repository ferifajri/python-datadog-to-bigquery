import calendar

from datetime import datetime, timedelta, date

def daterange(start_date, end_date):
   for n in range(int((end_date - start_date).days)):
      yield start_date + timedelta(n)
   # for n in range((end_date - start_date).days * 24 + 1):
   #    yield start_date + timedelta(hours=n)
      # print(start_date + timedelta(hours=n))

def getdate(start_date, end_date):
   for single_date in daterange(start_date, end_date):
      # print(single_date)
      ystart = single_date.strftime("%Y-%m-%d")
      yesterday = ystart
      yend = ystart

      # print(ystart)
      ystart = ystart + ' 00:00:00'
      ystart = datetime.strptime(ystart, "%Y-%m-%d %H:%M:%S")
      # print(ystart)
      ystarttime = str(ystart)
      ystarttime = '"' + ystarttime + '"'
      # ystart = ystart.timestamp()
      # ystart = int(ystart.strftime("%s"))
      # ystart = time.mktime(ystart.timetuple())
      ystart = calendar.timegm(ystart.timetuple())
      # print(ystart)
      # print(ystarttime)

      yend = yend+' 23:59:59'
      yend = datetime.strptime(yend, "%Y-%m-%d %H:%M:%S")
      yendtime = str(yend)
      yendtime = '"'+yendtime+'"'
      # yend = int(yend.strftime("%s"))
      yend = calendar.timegm(yend.timetuple())
      # print (yend)
      # print(yendtime)

      return ystart,ystarttime,yend,yendtime

# yesterday = datetime.now() - timedelta(hours=24)
# yesterday = datetime.now() - timedelta(hours=2)
# yesterday = yesterday.strftime('%Y-%m-%d %H:00:00')
# yesterday = yesterday.strftime('%Y-%m-%d')
# today = datetime.now() - timedelta(hours=1)
# today = datetime.now() - timedelta(hours=1)
# today = today.strftime('%Y-%m-%d %H:00:00')
# today = today.strftime('%Y-%m-%d')
#
# getdate(yesterday, today)







def hourrange(start_date, end_date):
   while end_date > start_date:
      yield start_date
      start_date = start_date + timedelta(hours=1)

def gethour(hour):
      ystart = hour.strftime("%Y-%m-%d %H:00:00")
      file_date = hour.strftime("%Y-%m-%d")
      file_hour = hour.strftime("%H")
      yend = hour.strftime("%Y-%m-%d %H:59:59")

      ystart = datetime.strptime(ystart, "%Y-%m-%d %H:%M:%S")
      ystarttime = str(ystart)
      ystarttime = '"' + ystarttime + '"'
      ystart = calendar.timegm(ystart.timetuple())

      # yend = yend+' 23:59:59'
      yend = datetime.strptime(yend, "%Y-%m-%d %H:%M:%S")
      yendtime = str(yend)
      yendtime = '"'+yendtime+'"'
      # yend = int(yend.strftime("%s"))
      yend = calendar.timegm(yend.timetuple())
      # print (yend)
      # print(yendtime)

      return ystart,ystarttime,yend,yendtime,file_date,file_hour

# start_date = datetime.now() - timedelta(hours=3)
# str_start_date = datetime.strftime(start_date, '%Y-%m-%d %H:00:00')
# start_date = datetime.strptime(str_start_date, '%Y-%m-%d %H:00:00')
#
# end_date = datetime.now() - timedelta(hours=1)
# str_end_date = datetime.strftime(end_date, '%Y-%m-%d %H:00:00')
# end_date = datetime.strptime(str_end_date, '%Y-%m-%d %H:00:00')
#
# gethour(start_date, end_date)
# for hour in hourrange(start_date, end_date):
#    print(hour)

