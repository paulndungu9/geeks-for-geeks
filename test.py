from sqlite3 import Date


day=Date.today()
print(day)
from datetime import date
today=date.today()
print("Today's date:", today)
d1=today.strftime("%d/%m/%Y")
print("d1=", d1)
d2=today.strftime("%B %d, %Y")
print("d2 =", d2)
d3=today.strftime("%m/%d/%y")
print("d3 =", d3)
d4=today.strftime("%b-%d-%Y")
print("d4 =", d4)
from datetime import datetime
now = datetime.now()
print("now =", now)
dt_string=now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
from datetime import datetime
current_time=now.strftime("%H:%M:%S")
print("current_time =", current_time)
import time
print(time.asctime(time.strptime('2015 50 1', '%Y %W %w')))