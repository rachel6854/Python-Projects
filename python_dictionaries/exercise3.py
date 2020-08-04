country_populations = {}
country_populations["Ghana"] = 28
country_populations["Brazil"] = 209
country_populations["Mongolia"] = 3
country = "Ghana"
print(country + " is a ", end="")
print("big" if country_populations[country] > 50 else "small" + " country")
