# continues from previous script, source https://www.programiz.com/python-programming/property

# The property Class
# A pythonic way to deal with the above problem is to use the property class. Here is how we can update our code:

# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


#The last line of the code makes a property object temperature.
# Simply put, property attaches some code (get_temperature and set_temperature) to the member attribute accesses (temperature).

#Let's use this update code:

human = Celsius(37)  # Setting value...  - tova se printva zaradi chastta s  temperature = property(get_temperature, set_temperature)

print(human.temperature) # Getting value...
                         # 37

print(human.to_fahrenheit()) # Getting value...
                            # 98.60000000000001
#human.temperature = -300 # ValueError: Temperature below -273.15 is not possible


# As we can see, any code that retrieves the value of temperature will automatically call get_temperature()
# instead of a dictionary (__dict__) look-up. Similarly, any code that assigns a value to temperature will
# automatically call set_temperature().

#We can even see above that set_temperature() was called even when we created an object. # human = Celsius(37) returned Setting value...

# Can you guess why?

# The reason is that when an object is created, the __init__() method gets called.
# This method has the line self.temperature = temperature. This expression automatically calls set_temperature().

#Similarly, any access like c.temperature automatically calls get_temperature().
# This is what property does. Here are a few more examples.

# >>> human.temperature
# Getting value
# 37
# >>> human.temperature = 37
# Setting value
#
# >>> c.to_fahrenheit()
# Getting value
# 98.60000000000001


# By using property, we can see that no modification is required in the implementation of the value constraint.
# Thus, our implementation is backward compatible.

#Note: The actual temperature value is stored in the private _temperature variable.
# The temperature attribute is a property object which provides an interface to this private variable.

# The @property Decorator
# In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is:

# property(fget=None, fset=None, fdel=None, doc=None)

# where,
#
# fget is function to get value of the attribute
# fset is function to set value of the attribute
# fdel is function to delete the attribute
# doc is a string (like a comment)

# As seen from the implementation, these function arguments are optional. So, a property object can simply be created as follows.

# >>> property()
# <property object at 0x0000000003239B38>

# A property object has three methods, getter(), setter(), and deleter()
# to specify fget, fset and fdel at a later point. This means, the line:
#temperature = property(get_temperature,set_temperature)

# can be broken down as:

# # make empty property
# temperature = property()
# # assign fget
# temperature = temperature.getter(get_temperature)
# # assign fset
# temperature = temperature.setter(set_temperature)


# These two pieces of codes are equivalent.
#
# Programmers familiar with Python Decorators can recognize that the above construct can be implemented as decorators.
#
# We can even not define the names get_temperature and set_temperature as they are unnecessary and pollute the class namespace.
#
# For this, we reuse the temperature name while defining our getter and setter functions. Let's look at how to implement this as a decorator:


# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

#coldest_thing = Celsius(-300)

# The above implementation is simple and efficient. It is the recommended way to use property.