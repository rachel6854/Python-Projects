import json

json_file = open("pokemon.json", "r")
pokemon_data = json.load(json_file)
pokemon_data = list(map(
    lambda item: item["name"], pokemon_data))
print(pokemon_data)
