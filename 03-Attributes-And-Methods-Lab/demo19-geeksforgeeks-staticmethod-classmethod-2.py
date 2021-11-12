# Class method vs Static Method

# A class method takes cls as first parameter while a static method needs no specific parameters.
# A class method can access or modify class state while a static method can’t access or modify it.
# In general, static methods know nothing about class state. They are utility type methods that
# take some parameters and work upon those parameters. On the other hand class methods must have class as parameter.
# We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to
# create a static method in python.
# When to use what?
#
# We generally use class method to create factory methods. Factory methods return class object ( similar to a constructor )
# for different use cases.
# We generally use static methods to create utility functions.
# How to define a class method and a static method?
#
# To define a class method in python, we use @classmethod decorator and to define a static method we use @staticmethod decorator.
# Let us look at an example to understand the difference between both of them. Let us say we want to create a class Person.
# Now, python doesn’t support method overloading like C++ or Java so we use class methods to create factory methods.
# In the below example we use a class method to create a person object from birth year.
#
# As explained above we use static methods to create utility functions. In the below example we use a static method to
# check if a person is adult or not.
#
# Implementation

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a class method to create a Person object by birth year.

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

        # a static method to check if a Person is adult or not.

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 2005)

print(person1.age) # 21
print(person2.age) # 15

# print the result
print(Person.isAdult(22)) # True
print(Person.isAdult(person1.age)) # True
print(Person.isAdult(person2.age)) # False


