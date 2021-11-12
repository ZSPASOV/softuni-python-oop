# To access and change private variables, accessor (getter) and mutators(setter)
# methods should be used, as they are part of the class

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def info(self):
        print(self.name)
        print(self.__age)

    def get_age(self):
        print(self.__age)

    def set_age(self, age):
        self.__age = age

person = Person('Peter', 25)

# accessing data using class method
person.info()	# Peter
		# 25

# changing age using setter
person.set_age(26)
person.get_age()	# 26
