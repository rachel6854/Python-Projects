try:
    age = int(input("How old are you? "))
    if age < 0 or age > 120:
        raise ValueError("Invalid age")
except ValueError as exp:
    print(exp, ": you need enter age between 0-120")
