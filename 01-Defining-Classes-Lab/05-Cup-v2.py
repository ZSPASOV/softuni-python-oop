class Cup:

    def __init__(self, size: int, quantity: int, *args, **kwargs): # args i kwargs sa optional
        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self, milliliters):
        new_quantity = self.quantity + milliliters
        if new_quantity <= self.size:
            self.quantity = new_quantity

cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())