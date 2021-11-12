# An individual object of a certain class
    # The instantiation operation creates an empty object
    # Тo create objects with instances customized to a specific initial state, we can define a special method named __init__()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


George = Person('George', 25)

# The only operations understood by instance objects are attribute references
# There are two kinds of valid attribute names:
    # data attributes
    # methods
