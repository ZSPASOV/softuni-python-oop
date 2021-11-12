# We can avoid the domino effect if the application changes by splitting the class:
    # create another class that will handle the responsibility of storing a student to a database

class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class StudentRecords:
    def get_student(self, id):
        pass

    def register(self, student):
        pass
