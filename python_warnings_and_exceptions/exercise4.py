def divide(x, y):
    print(f'{x}/{y} is {x / y}')


try:
    divide(3, 0)
except ZeroDivisionError as exp:
    print("Math error:", exp)

try:
    divide("j", 9)
except TypeError as exp:
    print("The first parameter should be a number:", exp)

try:
    divide(9, "l")
except TypeError as exp:
    print("The second parameter should be a number:", exp)


except(TypeError,ValueError) as exp:
    print("You entered invalid parameters:",exp)
