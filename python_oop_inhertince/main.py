import random
from office import Office

names_of_managers = ["Manager1", "Manager2", "Manager3"]
names_of_clerks = [["Clerk1", "Clerk2"], ["Clerk3", "Clerk4"], ["Clerk5", "Clerk6"]]
names_of_cleaners = ["Cleaner1", "Cleaner2", "Cleaner3"]
names_of_skills = ["Skill1", "Skill2", "Skill3", "Skill4", "Skill5", "Skill6", "Skill7", "Skill8"]

office = Office()
for i in range(3):
    office.hire_manager(names_of_managers[i])
    for j in range(2):
        (office.managers[i]).hire_employee(names_of_clerks[i][j])
        for k in range(3):
            office.managers[i].employees[j].add_skill(names_of_skills[random.randint(0, 7)])

for i in range(3):
    office.hire_cleaner(names_of_cleaners[i])
office.start_work_day()
