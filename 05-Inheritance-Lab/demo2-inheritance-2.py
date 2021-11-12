class Person:
    def __init__(self, name):
        self.name = name


    def say_my_name(self):
        return self.name


class Student(Person): # - subclassing
    def __init__(self, name, faculty_number): # tva e primer kak moje da prezapishem inicializaciq i da imame pove4e argumenti ot klasa ot koito se nasledqva
        self.name = name
        self.faculty_number = faculty_number


student = Student('Ivan Ivanov', 'F123456')
print(student.say_my_name()) # Ivan Ivanov, pak si 4ete nasledenite metodi