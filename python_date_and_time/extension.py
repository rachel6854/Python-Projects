import datetime

current_date = datetime.date.today()
user_input = input('please enter your birthday in DD-MM-YYYY format ')

birthday = datetime.datetime.strptime(user_input, '%d-%m-%Y').date()
months = birthday.month - current_date.month
days = birthday.day - current_date.day

current_time=datetime.datetime.now().strftime("%H:%M:%S:%f")
hours=24-int(current_time[:2])
minutes=60-int(current_time[3:5])
seconds=60-int(current_time[6:8])
micro_second=999999-int(current_time[9:])


print('your next birthday is in ' + str(months) + ' months ' + str(days) + ' days '+str(hours)+' hours '+str(seconds)+' seconds and '+str(micro_second)+' micro seconds')
