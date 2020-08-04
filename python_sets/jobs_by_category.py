import json

json_file = open("nyc_jobs.json", "r")
json_list = json.load(json_file)


def find_agency_by_category(category):
    return list(filter(lambda item: category in item.get("job_category", ""), json_list))


def find_jobs_by_category(categories_):
    list_ =[]
    for category in categories_:
        list_+=find_agency_by_category(category)
    return set(map(lambda item: item["job_id"],list_))


categories = ["Technology", "Engineering", "Data & Innovation"]
print(len(find_jobs_by_category(categories)))
