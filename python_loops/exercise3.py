list = [0]
sum = 0

for i in range(1, 101):
    list.append(i)

for i in list:
    if i < 20 or i > 80:
        sum += i
print(sum)
