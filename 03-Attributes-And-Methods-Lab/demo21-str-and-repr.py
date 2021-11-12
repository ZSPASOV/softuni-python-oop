# https://www.journaldev.com/22460/python-str-repr-functions


class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

p = Person('Pankaj', 34)

print(p.__str__()) # <__main__.Person object at 0x000000000267B4C0>
print(p.__repr__()) # <__main__.Person object at 0x000000000267B4C0>

# As you can see that the default implementation is useless. Let’s go ahead and implement both of these methods

class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        return {'name':self.name, 'age':self.age}

    def __str__(self):
        return 'Person(name='+self.name+', age='+str(self.age)+ ')'

# Notice that we are returning dict for __repr__ function. Let’s see what happens if we use these methods.

p = Person('Pankaj', 34)

# __str__() example
print(p) # Person(name=Pankaj, age=34)
print(p.__str__()) # Person(name=Pankaj, age=34)
#
s = str(p)
print(s) # Person(name=Pankaj, age=34)
#
# # __repr__() example
print(p.__repr__()) # {'name': 'Pankaj', 'age': 34}
print(type(p.__repr__())) # <class 'dict'>
# print(repr(p)) # TypeError: __repr__ returned non-string (type dict)

# Notice that repr() function is throwing TypeError since our __repr__ implementation is returning dict and not string.
#
# Let’s change the implementation of __repr__ function as follows:

class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        return '{name:' + self.name + ', age:' + str(self.age) + '}'

    def __str__(self):
        return 'Person(name='+self.name+', age='+str(self.age)+ ')'

# Now it’s returning String, and the new output for object representation calls will be:
p = Person('Pankaj', 34)
print(p.__repr__()) # {'name': 'Pankaj', 'age': 34}
print(type(p.__repr__())) # <class 'dict'>
print(repr(p)) # TypeError: __repr__ returned non-string (type dict)


# Difference between __str__ and __repr__ functions
# __str__ must return string object whereas __repr__ can return any python expression.
# If __str__ implementation is missing then __repr__ function is used as fallback. There is no fallback if __repr__ function implementation is missing.
# If __repr__ function is returning String representation of the object, we can skip implementation of __str__ function.
# Summary
# Both __str__ and __repr__ functions are very similar. We can get the object representation in String format as well as other specific formats such as tuple and dict to get information about the object.