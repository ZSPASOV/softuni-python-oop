# To make a method or variable private you can do it by prefixing it with double underscores
# It is still possible to access the private variables/ methods from outside the class
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def info(self):
        print(self.name)
        print(self.__age)


person = Person('Peter', 25)
# accessing data using the class method
person.info()	# Peter # 25
# accessing data directly from outside
print(person.name)	 # Peter
print(person.__age) # AttributeError: 'Person' object has no attribute '__age'
