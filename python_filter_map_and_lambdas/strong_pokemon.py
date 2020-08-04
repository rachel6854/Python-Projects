import json

json_file = open("pokemon.json", "r")
pokemon_data = json.load(json_file)
heavy_pokemon = list(filter(lambda item: item["weight"] > 100, pokemon_data))
# print(len(heavy_pokemon))
