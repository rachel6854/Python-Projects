import random
import math

exchange_rate = random.uniform(3.5, 5.5)
sum = float(input("Please enter the amount of Shekels you would like to exchange."))
print("The exchange_rate: " + str(exchange_rate))
print("The number of Euros that should be returned to you: " + str(math.floor(sum * exchange_rate)))
