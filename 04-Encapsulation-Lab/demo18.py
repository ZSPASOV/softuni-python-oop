# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.__temperature = temperature

    def to_fahrenheit(self):
        return (self.__temperature * 1.8) + 32

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self.__temperature = value


# create an object
human = Celsius(37)

print(human.temperature) # 37

human.temperature = 40
print(human.temperature) # 40
print(human.to_fahrenheit()) # 104.0

#human.temperature = -300 # ValueError: Temperature below -273 is not possible

# print(human.temperature)
#
# print(human.to_fahrenheit())
#
# #coldest_thing = Celsius(-300)