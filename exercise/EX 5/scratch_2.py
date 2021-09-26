month_A = ["Apr","Jun","Sep","Nov"]
month_B = ["Jan","Mar","May","Jul","Aug","Oct","Dec"]
month_C = ["Feb"]

odd_day = 0

print("Number of month that have 30 days is",len(month_A),"months")

for x in month_A:
    if x in month_A:
        odd_day += (30/2)
    else:
        continue

print("Number of month that have 31 days is",len(month_B),"months")

for x in month_B:
    if x in month_B:
        odd_day += (30/2)
        odd_day += 1
    else:
        continue

print("Number of month that have 28 days is",len(month_C),"month")

for x in month_C:
    if x in month_C:
        odd_day += (28/2)
    else:
        continue

print("Odd days in year 2021 have",int(odd_day),"days")