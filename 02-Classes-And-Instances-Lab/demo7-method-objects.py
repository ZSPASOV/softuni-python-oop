# What exactly happens when a method is called?: x.say_hello()
    # the  method was called without an argument, even though the function definition for say_hello() specified an argument
    # the instance object is passed as the first argument of the function


class MyClass:
    number = 743

    def say_hello(self):
        return 'Hello'

x = MyClass()
print(x.say_hello()) # Hello

# Method Objects Definition

# When we reference a valid class attribute that is a function object
# a method object is created by packing the instance object and the function object

# If the method object is called with an argument list, a new argument list
# is constructed from the instance object and the argument list



