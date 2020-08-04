from employee import Employee
from clerk import Clerk


class Manager(Employee):
    def __init__(self, name, salary=20000):
        super().__init__(name, salary)
        self.employees = []

    def hire_employee(self, name):
        self.employees.append(Clerk(name))

    def work(self, office):
        # print(self.name+" is manager")
        for employee in self.employees:
            employee.work(office)
