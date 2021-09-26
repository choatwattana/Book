#2.0
from datetime import date, timedelta, datetime

curr = "1-1-2021"
end = "31-12-2021"
format = "%d-%m-%Y"
start_date = datetime.strptime(curr, format)
end_date = datetime.strptime(end, format)

step = timedelta(1)
num_mon = 0
off_days = ['Mon']

days = (end_date - start_date).days
for x in range(days):
    day = start_date.strftime("%a")
    if day in off_days:
        num_mon += 1
    start_date += step

print(num_mon)