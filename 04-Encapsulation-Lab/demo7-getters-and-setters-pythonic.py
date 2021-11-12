# The "pythonic" way of defining getters and setters is using properties
    # By defining properties, you can change the internal implementation of
    # a class without affecting the program

class Person:
    def __init__(self, age=0):
        self.__age = age # tova e editnato, v ppt e greshno

    @property
    def age(self):
        return self.__age

    @age.setter
    def set_age(self, age):
        if age < 18:
            self.__age = 18
        else:
            self.__age = age

person = Person(25)
print(person.age)	# 25
person.set_age = 10
print(person.age)	# 18
person.set_age = 30
print(person.age)	# 30
