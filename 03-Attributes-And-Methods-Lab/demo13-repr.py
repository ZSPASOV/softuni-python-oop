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


p = Person('Panyo', 31)

# __str__() example
print(p) # Person(name=Panyo, age=31)
print(p.__str__()) # Person(name=Panyo, age=31)

s = str(p)
print(s) # Person(name=Panyo, age=31)

# __repr__() example
print(p.__repr__()) # {name:Panyo, age:31}
print(type(p.__repr__())) # <class 'str'>
print(repr(p)) # {name:Panyo, age:31}