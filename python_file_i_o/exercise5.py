import json

json_file = open("test_reports.json", "r")
csv_file = open("test_report.csv", "r")
csv_list = csv_file.read().split("\n")[1:]

json_file = open("test_reports.json", "r")
json_list = json.load(json_file)

index = 1
with open("test_report.txt", "a+", encoding="utf-8") as txt_file:
    for report in csv_list:
        report_list = report.split(",")
        # print(report_list)
        txt_file.write(f'Report: {report_list[0]}\n')
        txt_file.write(f'Number: {index}\n')
        txt_file.write(f'Time: {report_list[1]}\n')
        txt_file.write(f'Owner: {report_list[2]}\n')
        txt_file.write(f'Category: {report_list[3]} - {report_list[4]}\n')
        txt_file.write("FAIL\n" if report_list[5] == "0" else "PASS\n")
        txt_file.write('======================================\n======================================\n﻿')
        index += 1
    for item in json_list:
        txt_file.write(f'Report: {item["name"]}\n')
        txt_file.write(f'Number: {index}\n')
        txt_file.write(f'Time: {item["time"]}\n')
        txt_file.write(f'Owner: {item["owner"]}\n')
        txt_file.write(f'Category: {item["cat"]} - {item["sub-cat"]}\n')
        txt_file.write("FAIL\n" if item["status"] == "0" else "PASS\n")
        txt_file.write('======================================\n======================================\n﻿')
        index += 1
