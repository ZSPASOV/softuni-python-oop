# ot edin base class nasledqvat nqkolko subclasses
class Animal:
    pass


class Monkey(Animal):
    pass


class Dog(Animal):
    pass

print(Animal.__subclasses__()) # [<class '__main__.Monkey'>, <class '__main__.Dog'>]