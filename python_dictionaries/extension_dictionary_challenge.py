def is_palindrome(string):
    return string == string[::-1]


def is_lower(string):
    return string.islower()


def is_all_digits(string):
    return string.isdigit()


def long(string):
    return len(string) > 15


def empty(string):
    return string == ""


def print_exit():
    print("GoodBye!!")
    #exit(0)


def show_options():
    print("The availble operations are:\n1 - Palindrome: Check if the input is palindrome\n2- Lower: Check if all "
          "characters in the input are lowercase\n3- Digits: Check if all characters in the input are digits\n4 - "
          "Long: Check if the input length is longer than 15 characters\n5 - Empty: Check if the input is empty\n6 - "
          "Exit: exit successfully from the application")
    return input("Please enter the number of the operation you choose:")


options = {"1": is_palindrome, "2": is_lower, "3": is_all_digits, "4": long, "5": empty}



while True:
    string = input("Enter an input")
    choose=show_options()
    if 0<int(choose)<6:
        print("The answer is: " + str(options[choose](string)))
    elif int(choose)==6:
        print_exit()
        break
    else:
        print("Wrong choose; please try again")