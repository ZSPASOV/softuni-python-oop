# demo ot Jordan
# We can avoid the domino effect if the application changes by splitting the class:
# create another class that will handle the responsibility of storing a student to a database

class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class StudentRegistry:
    def __init__(self):
        self.students = []

    def register(self, student: Student):
        self.students.append(student)

    # moje da imame pove4e ot edin metod, tova ne narushava SRP,
    # operaciite koito se izvurshvat trqbva da sa logicheski svurzani
    def unregister(self, student: Student):
        self.students.pop(self.students.find(student))


student = Student('Jordan')

registry = StudentRegistry()
registry.register(student)