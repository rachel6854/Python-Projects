import json
import csv

json_file = open("food_json.json", "r")
food_list = json.load(json_file)

with open("food_csv.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(["name", " protein", "fat", "carbohydrate", "sugars"])
    for food in food_list:
        data_in_list = [food.get("name", ""), (food.get("nutrition-per-100g", {})).get("protein", ""),
                        (food.get("nutrition-per-100g", {})).get("fat", ""),
                        (food.get("nutrition-per-100g", {})).get("carbohydrate", ""),
                        (food.get("nutrition-per-100g", {})).get("sugars", "")]
        csv_writer.writerow(data_in_list)
