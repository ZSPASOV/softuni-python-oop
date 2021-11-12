# A static method is a method that knows nothing about the class or instance it is called on
# It's easy to turn a method into a static method
# All we have to do is to add a line with @staticmethod in front of the method header
# To call a static method, we use the instance or the class

class Robot:
    __counter = 0 # protected attribute

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def robot_instances():
        return Robot.__counter

print(Robot.robot_instances())  # 0
x = Robot()
print(x.robot_instances())      # 1
y = Robot()
print(x.robot_instances())      # 2
print(Robot.robot_instances())  # 2
print(y.robot_instances())      # 2
z = Robot()
print(Robot.robot_instances())  # 3 - taka broim kolko instancii na class Robot sa suzdadeni

