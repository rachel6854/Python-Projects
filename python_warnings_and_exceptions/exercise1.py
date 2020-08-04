import math  # Error2- No import

dividend = float(input("Enter the dividend: "))  # Error2- The input is not a number
divisor = float(input("Enter the divisor: "))  # Error3- Divide by zero
quotient = dividend / divisor
print(math.floor(quotient))
