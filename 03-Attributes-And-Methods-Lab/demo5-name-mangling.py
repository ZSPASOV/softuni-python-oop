# da googlena kakvo e name mangling
# https://www.geeksforgeeks.org/name-mangling-in-python/

class Student:
    def __init__(self, name):
        self.__name = name

    def displayName(self):
        print(self.__name)


s1 = Student("Santhosh")
s1.displayName() # Santhosh

# Raises an error
# print(s1.__name) # AttributeError: 'Student' object has no attribute '__name'



# In the above example, the class variable __name is not accessible outside the class. It can be accessed only within the class.
# Any modification of the class variable can be done only inside the class.

# With the help of dir() method, we can see the name mangling process that is done to
# the class variable. The name mangling process was done by the Interpreter.
# The dir() method is used by passing the class object and it will return
# all valid attributes that belong to that object.


# Python program to demonstrate
# name mangling


class Student:
    def __init__(self, name):
        self.__name = name


s1 = Student("Santhosh")
print(dir(s1)) # ['_Student__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
print(s1.__dict__) # {'_Student__name': 'Santhosh'}

# The above output shows dir() method returning all valid attributes with
# the name mangling process that is done to the class variable __name.
# The name changed from __name to _Student__name.



# Accessing Name Mangled variables
# The name mangling process helps to access the class variables
# from outside the class. The class variables can be accessed by
# adding _classname to it. The name mangling is closest to private not exactly private

# Python program to demonstrate
# name mangling


class Student:
    def __init__(self, name):
        self.__name = name


s1 = Student("Santhosh")
print(s1._Student__name) # Santhosh

# The above class variable is accessed by adding the _classname to it.
# The class variable is accessed from outside the class with the name _Student__name.


# Name mangling with method overriding
# Due to name mangling, there is limited support for a valid use-case for
# class-private members basically to avoid name clashes of names with names defined
# by subclasses. Any identifier of the form __geek (at least two leading underscores
# or at most one trailing underscore) is replaced with _classname__geek, where classname
# is the current class name with leading underscore(s) stripped. As long as it occurs within
# the definition of the class, this mangling is done. This is helpful for letting subclasses
# override methods without breaking intraclass method calls.
# Let’s look at this example and try to find out how this underscore works:


# Python code to illustrate how mangling works
# With method overriding

class Map:
    def __init__(self):
        self.__geek()

    def geek(self):
        print("In parent class")

        # private copy of original geek() method

    __geek = geek


class MapSubclass(Map):

    # provides new signature for geek() but
    # does not break __init__()
    def geek(self):
        print("In Child class")

    # Driver's code


obj = MapSubclass() # In parent class
obj.geek() # In Child class