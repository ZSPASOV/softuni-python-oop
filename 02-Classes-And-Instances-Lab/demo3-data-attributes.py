# Data attributes do not need to be declared
# like local variables they spring into existence when they are first assigned to

class Laptop:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

laptop = Laptop('Swift', 'ACER')
laptop.ram = 8
print(laptop.ram) # 8
del laptop.ram
print(laptop.ram) # AttributeError: 'Laptop' object has no attribute 'ram'

