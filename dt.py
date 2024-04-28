'''Module for Date and time'''
#importing datetime
import datetime

#class for date
def getDate():
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    return str(now)   #returning it as string

#class for time
def getTime():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return str(now)   #returning it as string

#class for receipt (after borrowing or receiving)
def getDat():
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    return str(now) #returning it as string

#class for return date
def retdat():
    from datetime import datetime, timedelta #importing timedelta to timeskip
    now = datetime.now()
    td = timedelta(days = 10)                #duration = 10 days
    retdt = now + td
    retdt = retdt.strftime("%Y-%m-%d")       # YYYY-MM-DD format
    #print(retdt)
#retdat()
    return str(retdt)
