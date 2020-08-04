# time: 06:24:48
# current1: 07/14/2020, 01:32:02
# current2: 14/07/2020, 01:32:02
import datetime

print(datetime.datetime.now().strftime("time: %H:%M:%S"))
print(datetime.datetime.now().strftime("current1: %m/%d/%Y, %H:%M:%S"))
print(datetime.datetime.now().strftime("current2: %d/%m/%Y, %H:%M:%S"))