# Classes provide means of building data functionality together
# Classes create new types of objects that allow instances of that type to be made
# Each class instance can have attributes for maintaining its state
# Class instances can also have methods for modifying its state

class Person: # class name
    def __init__(self, name, age): # class method
        self.name = name
        self.age = age # instance attribute

me = Person('Panyo', 31)
print(me.name) # Panyo
print(me.age) # 31