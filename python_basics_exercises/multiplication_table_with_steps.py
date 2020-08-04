num = int(input("Please enter integer"))
step = int(input("Please enter step"))
for i in range(0,num+1,step):
    for j in range(0,num+1,step):
        print(i * j , end="  ")
    print()
