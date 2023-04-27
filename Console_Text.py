import os
import datetime
class Console:
    #file for console calls when messaging user
    def Get_Time():
        today = datetime.datetime.now()
        date_Time = today.strftime("%m/%d/%Y %H:%M:%S:")
        return date_Time
