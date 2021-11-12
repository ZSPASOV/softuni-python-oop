class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name,
        self.age = age

    def __str__(self):
        return 'wagwan'

a = Person('Panyo', 31)
print(a) # wagwan

print(a.__repr__)