import json

json_file = open("nyc_jobs.json", "r")
json_list = json.load(json_file)


def junior_jobs_in_brooklin():
    list_ = list(
        filter(lambda item: item["career_level"] == "Entry-Level" and "Broadway" in item["work_location"], json_list))
    return set(map(lambda item: item["agency"], list_))


print(junior_jobs_in_brooklin())
