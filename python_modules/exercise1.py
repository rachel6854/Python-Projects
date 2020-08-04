import calendar

count = 0

print("2010 is", "" if calendar.isleap(2010) else "not ", "a leap year")

print("2020 is", "" if calendar.isleap(2020) else "not ", "a leap year")

for i in range(2021, 2081):
    if calendar.isleap(i):
        count += 1
print("Number of leap years between 2020 and 2080: " + str(count))
print("March 14, 2028 will be on "+calendar.day_name[calendar.weekday(2028,3,14)])

