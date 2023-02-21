import os
import datetime

#file for console calls when messaging user
def GetTime():
    today = datetime.datetime.now()
    dateTime = today.strftime("%m/%d/%Y %H:%M:%S:")
    return dateTime
