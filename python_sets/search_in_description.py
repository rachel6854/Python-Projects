import json

json_file = open("nyc_jobs.json", "r")
json_list = json.load(json_file)

def find_jobs_by_word(word):
    return list(filter(lambda item: word in item["job_description"], json_list))


print(len(find_jobs_by_word("experience")))  # 165
