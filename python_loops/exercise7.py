salaries = [1200, 2500, 1800, 1600, 1800, 700, 3200, 1500, 1300, 1300, 850, 1900]
average = sum(salaries) / len(salaries)
new_list = []
for i in salaries:
    if i > average:
        new_list.append(i)
new_average = sum(new_list) / len(new_list)
print(new_average)
