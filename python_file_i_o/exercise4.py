import json
import csv

data = open("ikea.txt", "r")
data_list = data.read().replace("\n", "-").split("-")

dict_json = []
for i in range(0, len(data_list), 2):
    dict_json.append({data_list[i]: data_list[i + 1]})
with open("json_list.json", "w") as json_file:
    json.dump(dict_json, json_file)
with open("csv_list.csv","w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["item","price"])
    for i in range(0,len(data_list),2):
        data_in_list = [data_list[i],data_list[i+1]]
        csv_writer.writerow(data_in_list)
