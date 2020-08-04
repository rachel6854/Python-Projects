# "aGUiLSCMepk" = > "aCeGikLUSpM"
string = "ArYnjTdsV"

lower = ""
upper = ""
less = ""
more = ""
for i in string:
    if i.islower():
        lower += i
    else:
        upper += i
    if ('a' <= i < 'm') or ('A' <= i < 'M'):
        less += i
    else:
        more += i

replace_string1 = ''.join(sorted(lower)[::-1]) + ''.join(sorted(upper)[::-1])
print(replace_string1)
replace_string2 = ''.join(sorted(less, key=lambda x: x.lower())) + ''.join(sorted(more, key=lambda x: x.lower())[::-1])
# print(replace_string2)
