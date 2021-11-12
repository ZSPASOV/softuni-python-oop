# A private method is a class method that should only be called from inside the class where it is defined
# To define a private method prefix the name with double underscore

class Person:
    def __init__(self):
        self.first_name = 'Peter'
        self.last_name = 'Parker'

    def __full_name(self):
        return f'{self.first_name} {self.last_name}'

    def info(self):
        return self.__full_name()


person = Person()
print(person.info())	              # Peter Parker
#print(person.__full_name())	   # AttributeError
print(person._Person__full_name())  # Peter Parker - tova ne e dobra praktika, nari4a se name mungling



