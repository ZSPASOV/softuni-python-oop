class Laptop:
    def __init__(self, brand):
        self.brand = brand

winlap = Laptop('Lenovo')
macbook = Laptop('Macbook')

winlap.ram = 8
Laptop.ram = 16

print(winlap.ram) # 8 tuk ram na nivo instanciq e s prioritet
print(Laptop.ram) # 16 tuk poneje nqma ram na nivo instanciq proverqva za ram v class Laptop i tam sme dobavili da e 16
