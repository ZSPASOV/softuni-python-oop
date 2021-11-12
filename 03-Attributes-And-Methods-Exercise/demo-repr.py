class Customer:


    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        dvds = ', '.join([d.name for d in self.rented_dvds])
        return (f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} "
                f"rented DVD's ({dvds})")


panyo = Customer('Panyo', 31, 22222)

a = repr(panyo)
print(a) # 22222: Panyo of age 31 has 0 rented DVD's ()
print(panyo.__repr__()) # 22222: Panyo of age 31 has 0 rented DVD's ()
print(repr(panyo)) # 22222: Panyo of age 31 has 0 rented DVD's ()