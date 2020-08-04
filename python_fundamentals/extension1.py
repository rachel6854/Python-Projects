mass = 1
# c=299792458
celeritas = 300000000
energy_of_kilogram = mass * (celeritas ** 2)
energy_of_nenogram = energy_of_kilogram / (10 ** 12)
print("The energy is: " + str(energy_of_nenogram) + " joules")
