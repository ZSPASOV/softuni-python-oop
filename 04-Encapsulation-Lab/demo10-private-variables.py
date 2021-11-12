# A private variable can only be changed within a class method
# Double underscore prefixed to a variable makes it private or non-public
# Objects can hold crucial data and you do not want that data to be changeable from anywhere in the code

class Car:
    def __init__(self):
        self.__max_speed = 200

    def drive(self):
        print('driving max speed ' + str(self.__max_speed))


red_car = Car()
red_car.drive() # driving max speed 200
red_car.__max_speed = 10  # won't change because it is private
red_car.drive() # driving max speed 200

# change the private variable with getters/setters
class Car:
    def __init__(self):
        self.__max_speed = 200

    def drive(self):
        print('driving max speed ' + str(self.max_speed))

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        self.__max_speed = value

red_car = Car()
red_car.drive() # driving max speed 200
red_car.max_speed = 10 # changes the speed
red_car.drive() # driving max speed 10
