def get_list_element(my_list, index):
    try:
        print(my_list[index])
    except IndexError as exp:
        print("You have given wrong index:", exp)


get_list_element(["hello"], 2)
