# https://www.programiz.com/python-programming/property

#In this tutorial, you will learn about Python @property decorator; a pythonic way
# to use getters and setters in object-oriented programming.

# Python programming provides us with a built-in @property decorator which makes usage of getter and setters
# much easier in Object-Oriented Programming.
#
# Before going into details on what @property decorator is, let us first
# build an intuition on why it would be needed in the first place.


# Class Without Getters and Setters
# Let us assume that we decide to make a class that stores the temperature in
# degrees Celsius. It would also implement a method to convert the temperature
# into degrees Fahrenheit. One way of doing this is as follows:

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# We can make objects out of this class and manipulate the temperature attribute as we wish:

# Basic method of setting and getting attributes in Python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# Create a new object
human = Celsius()

# Set the temperature
human.temperature = 37

# Get the temperature attribute
print(human.temperature) # 37

# Get the to_fahrenheit method
print(human.to_fahrenheit()) # 98.60000000000001


# The extra decimal places when converting into Fahrenheit is due to the floating point
# arithmetic error. To learn more, visit Python Floating Point Arithmetic Error.

# Whenever we assign or retrieve any object attribute like temperature as shown above,
# Python searches it in the object's built-in __dict__ dictionary attribute.

print(human.__dict__) # {'temperature': 37}

# Therefore, man.temperature internally becomes man.__dict__['temperature'].


#Using Getters and Setters
#Suppose we want to extend the usability of the Celsius class defined above.
# We know that the temperature of any object cannot reach below -273.15 degrees Celsius (Absolute Zero in Thermodynamics)

# Let's update our code to implement this value constraint.

# An obvious solution to the above restriction will be to hide the attribute temperature (make it private)
# and define new getter and setter methods to manipulate it. This can be done as follows:

# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

# As we can see, the above method introduces two new get_temperature() and set_temperature() methods.
#
# Furthermore, temperature was replaced with _temperature. An underscore _ at the beginning is used to denote protected variables in Python.


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature()) # 37

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit()) # 98.60000000000001

# new constraint implementation
#human.set_temperature(-300) # ValueError: Temperature below -273.15 is not possible.

# Get the to_fahreheit method
print(human.to_fahrenheit()) # 98.60000000000001

#This update successfully implemented the new restriction.
# We are no longer allowed to set the temperature below -273.15 degrees Celsius.


# However, the bigger problem with the above update is that all
# the programs that implemented our previous class have to modify their code
# from obj.temperature to obj.get_temperature() and all expressions like obj.temperature = val to obj.set_temperature(val).

#This refactoring can cause problems while dealing with hundreds of thousands of lines of codes.

#All in all, our new update was not backwards compatible. This is where @property comes to rescue.


