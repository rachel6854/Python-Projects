num = int(input("Please enter integer"))
for i in range(num+1):
    for j in range(num+1):
        print(i * j, end="  ")
    print()
