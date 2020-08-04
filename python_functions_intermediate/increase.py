def increase(key, ammount=1):
    def ret_func(obj):
        obj[key] += ammount

    return ret_func


employee = {
    "name": "Momo",
    "age": 61,
    "salary": 10000
}
func1 = increase("age")
func1(employee)

func2 = increase("salary", 10000)
func2(employee)

# print(employee)

func3 = increase("salary", 1000)
copy_of_employee = employee
for i in range(0, 70 - 61, 2):
    func3(copy_of_employee)
print("Momo's salary when he retires: " + str(copy_of_employee["salary"]))
