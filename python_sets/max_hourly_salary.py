# Find out what is the max salary for jobs that are hourly but not Entry-Level.
import json

json_file = open("nyc_jobs.json", "r")
json_list = json.load(json_file)


def max_hourly_salary():
    list_ = list(
        filter(lambda item: item["career_level"] != "Entry_Level" and item["salary_frequency"] == "Hourly", json_list))
    return max(list_, key=lambda item: item["salary_range_from"])["salary_range_from"]


print(max_hourly_salary())
