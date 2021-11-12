# A class method, on the other hand, is a method that gets passed the class it was called on (or instance)
# This is useful when you want the method to be a factory for the class
# All we have to do is to add a line with @classmethod in front of the method header

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birthYear):
        return cls(name, date.today().year - birthYear) # tva e sushtoto vse edno Person(name, date.today().year - birthYear), suzdava instanciq na class Person

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

john = Person.from_birth_year('John',  1985)
john.display()  # John's age is: 35

print(john.age) # 35
# classmethod-a v sluchaq e kato factory (konstruktor) za instanciq
# suzdava instanciq john na class Person s atribut name = John i age = 35

# classmethod e polezno kogato iskame da suzdavame metodi koito se izvikvat direktno vurhu class-a
