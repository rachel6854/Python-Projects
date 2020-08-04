import random
from employee import Employee
from document import Document


class Clerk(Employee):
    def __init__(self, name, salary=15000):
        super().__init__(name, salary)
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def work(self, office):
        num_of_new_documents = random.randint(1, 10)
        for i in range(num_of_new_documents):
            type_ = random.choice(self.skills)
            document = Document(self.name, type_)
            office.add_document(document)
        print(self.name + " added " + str(num_of_new_documents) + " documents")
