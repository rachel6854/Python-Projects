import json

json_file = open("nyc_jobs.json", "r")
json_list = json.load(json_file)

def salaries_in_range():
    list_ = list(
        filter(lambda item: float(item["salary_range_from"]) >= 17 and float(item["salary_range_to"]) <= 21, json_list))
    return set(map(lambda item: item["agency"], list_))


print(salaries_in_range())
