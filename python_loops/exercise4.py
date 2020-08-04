equipment = ["hammer", "ruler", "torch", "scissors", "screwdriver", "scissors", "torch", "hammer", "hammer", "ruler"]
most_common_item = ""
highest_count = 0

for item in equipment:
    count_of_item = equipment.count(item)
    if count_of_item > highest_count:
        most_common_item = item
        highest_count=count_of_item

print("The item that appears the most in the list is " + most_common_item)
