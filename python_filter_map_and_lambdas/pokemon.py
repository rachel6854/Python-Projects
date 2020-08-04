import json

json_file = open("pokemon.json", "r")
pokemon_data = json.load(json_file)
pokemon_data = list(map(
    lambda item: {"id": item["id"], "name": item["name"], "type": item["type"], "weight": item["weight"],
                  "height": item["height"],
                  "weaknesses": item["weaknesses"]}, pokemon_data))
print(pokemon_data[0])
