# Create a class called Cup. Upon initialization it should receive size and quantity
# (a number representing how much liquid is in it). The class should also have a method
# called fill(milliliters) which will increase the amount of liquid in the cup with the
# given milliliters (if there is space in the cup, otherwise ignore). The cup should also
# have a status() method which will return the amount of free space left in the cup.

# my version
class Cup:

    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, to_fill: int):
        self.to_fill = to_fill
        if self.quantity + self.to_fill <= self.size:
            self.quantity += self.to_fill

    def status(self):
        self.amount_left = self.size - self.quantity
        return self.amount_left

cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
