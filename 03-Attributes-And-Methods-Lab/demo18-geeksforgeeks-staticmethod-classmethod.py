# class method vs static method in Python
# Last Updated: 19-11-2020
# Class Method
#
# The @classmethod decorator, is a builtin function decorator that
# is an expression that gets evaluated after your function is defined.
# The result of that evaluation shadows your function definition.
# A class method receives the class as implicit first argument, just like an instance method receives the instance
# Syntax:

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
# fun: function that needs to be converted into a class method
# returns: a class method for function.

# A class method is a method which is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
# It can modify a class state that would apply across all the instances of the class.
# For example it can modify a class variable that will be applicable to all the instances.

# Static Method
# A static method does not receive an implicit first argument.
# Syntax:

class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
# returns: a static method for function fun.

# A static method is also a method which is bound to the class and not the object of the class.
# A static method can’t access or modify class state.
# It is present in a class because it makes sense for the method to be present in class.