import datetime

def getDay():
    currentDate = datetime.date.today()
    return currentDate.strftime("%A")



    