from cleaner import Cleaner
from manager import Manager


class Office:
    def __init__(self):
        self.documents = []
        self.managers = []
        self.cleaners = []

    def hire_cleaner(self, name: str):
        self.cleaners.append(Cleaner(name))

    def hire_manager(self, name):
        self.managers.append(Manager(name))

    def add_document(self, document):
        self.documents.append(document)

    def start_work_day(self):
        for manager in self.managers:
            manager.work(self)
        for cleaner in self.cleaners:
            cleaner.work()
