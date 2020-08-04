###לא גמור!!!!!!!!!!!!

#לא צריך להגיש
import re
from collections import defaultdict

txt_file=open("cornfield.txt","r")
txt_list=txt_file.readlines()
list_=[]
d=defaultdict(int)
for i in txt_list:
    list_.append(re.sub('[^0-9]+', ' ', i).split(" ")[1:6])
for rectangle in list_:
    for i in range(int(rectangle[3])):
        for j in range(int(rectangle[4])):
            (d[i])[j]+=1
print(d)
#print(list_)