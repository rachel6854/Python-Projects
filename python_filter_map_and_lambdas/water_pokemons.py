import json

json_file = open("pokemon.json", "r")
pokemon_data = json.load(json_file)
weak_against_water_pokemon = list(
    map(lambda item: item["name"], filter(lambda item: "Water" in item["weaknesses"], pokemon_data)))
print(weak_against_water_pokemon)

