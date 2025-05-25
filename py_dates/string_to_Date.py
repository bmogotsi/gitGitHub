#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 

# add a day to a date field
from datetime import datetime, timedelta, date
import pathlib, re

###############################################################
# https://app.datacamp.com/learn/tutorials/converting-strings-datetime-objects
from datetime import date
# create a date object representing March 1, 2023
start_date = date(2023, 3, 1)

# extract information such as the year, month, and day
year = start_date.year
month = start_date.month
day = start_date.day

today = date.today() # https://www.geeksforgeeks.org/get-current-date-using-python/
thisYear = today.year
nextYear, lastYear = (thisYear+1, thisYear-1)

# get the day of the week (Note: Monday is coded as 0, and Sunday as 6)
weekday = start_date.weekday()

# the date can be formatted as a string if needed
date_str = start_date.strftime('%Y-%m-%d')

###############################################################
from datetime import time
# create a time object with the microsecond granularity
end_time = time(15, 45, 30, 500000)

# get the hour and minute
hour = end_time.hour
minute = end_time.minute
second = end_time.second
microsecond = end_time.microsecond
###############################################################
from datetime import datetime

# create a datetime object representing March 1, 2023 at 9:30 AM
start_datetime = datetime(2023, 3, 1, 9, 30)

# get the year, month, day, hour, and minute
year = start_datetime.year
month = start_datetime.month
day = start_datetime.day
hour = start_datetime.hour
minute = start_datetime.minute
###############################################################
# 4. datetime.timedelta
#This class represents a duration or time interval and provides methods for working with time intervals, 
# such as adding or subtracting time intervals from dates or times.

from datetime import timedelta

# create a timedelta object representing 3 hours and 15 minutes
event_duration = timedelta(hours=3, minutes=15)

# get the total duration in seconds
event_duration_seconds = event_duration.total_seconds()

# add the duration to a start time to get an end time
event_start_time = datetime(2023, 3, 1, 18, 15)
event_end_time = event_start_time + event_duration
###############################################################
# Convert a String to a datetime Object in Python Using datetime.strptime()
# In Python, we can use the datetime.strptime() method to convert a string to a datetime object. 
# The strptime() method takes two arguments: 
#       the string to be converted 
#       and a format string specifying the input string's format

# The format string uses a combination of formatting codes to represent the various components of the date and time. Here are some of the most commonly used formatting codes:

# %Y: 4-digit year
# %y: 2-digit year
# %m: 2-digit month (01-12)
# %d: 2-digit day of the month (01-31)
# %H: 2-digit hour (00-23)
# %M: 2-digit minute (00-59)
# %S: 2-digit second (00-59)
# %f:	Microsecond	234567

# Converting a string in a specific format to a datetime object
from datetime import datetime

# Example with the standard date and time format
date_str = '2023-02-28 14:30:00'
date_format = '%Y-%m-%d %H:%M:%S'

date_obj = datetime.strptime(date_str, date_format)
print(date_obj)

# Example with a different format

date_str = '02/28/2023 02:30 PM'
date_format = '%m/%d/%Y %I:%M %p'

date_obj = datetime.strptime(date_str, date_format)
print(date_obj)

# In the first example, we have a string representing a date and time in the format ‘YYYY-MM-DD HH:MM:SS’, 
# and for the second example in a different format, ‘MM/DD/YYYY HH:MM AM/PM’.

# For both cases, after we specify the correct format string as the second argument to strptime() to receive the correct datetime object.
###############################################################
# Converting a string with timezone information to a datetime object

from datetime import datetime

date_str = '2023-02-28 14:30:00+05:30'
date_format = '%Y-%m-%d %H:%M:%S%z'

date_obj = datetime.strptime(date_str, date_format)
print(date_obj)

###############################################################
###############################################################
try:
    file = 'prjHTMLParse_Selinium_Chrome_WSB_output2024_11_29-21_39_21_205927.csv'
    file_extension = pathlib.Path(file).suffix
    len1=len(str('prjHTMLParse_Selinium_Chrome_WSB_output'))
    lenFile = len(str(file).strip())


    if file_extension == '.csv' and file[0:len1]=='prjHTMLParse_Selinium_Chrome_WSB_output':
        # dateFile = str(file[len1+1:lenFile])
        s = str(file[len1:lenFile]).strip(".csv") # 2024_11_29-21_39_21205927

        s1 = s.replace("-", " ").replace("_", "-", 2).replace("_", ":", 2).replace("_", ".", 1)
        date_str = s1 # 2024-11-29 21:39:21.205927
        date_format = '%Y-%m-%d %H:%M:%S.%f'                     
        date_stamp = datetime.strptime(date_str, date_format) # datetime.datetime(2024, 11, 29, 21, 39, 21, 205927)

        date_obj = datetime.strptime(date_str, date_format)

        fileTimeStamp =  str(datetime.strftime(date_stamp, '%Y_%m_%d-%H_%M_%S%f'))

        #get date
        day = 2
        dateRegex= re.compile(r'\d\d\d\d-\d\d-\d\d')
        mo= dateRegex.search(date_str)
        if  mo.group(0) != '':
            s=str(mo.group(0))
            datem = datetime.strptime(s, "%Y-%m-%d")
            modified_date = datem + timedelta(days=day)
            date_obj_s = datetime.strptime(s, "%Y-%m-%d")
            if modified_date.weekday() > 4:
                delay = 45
            else:
                delay=20 #5 seconds

    exit
except Exception as e:
    print("Exception String is...:     " + str(e))