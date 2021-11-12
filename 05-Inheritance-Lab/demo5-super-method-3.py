class Human:
    def __init__(self, name):
        self.name = name


    def say_my_name(self):
        return self.name


class Raver(Human):
    def say_my_name(self):
        res = super().say_my_name()
        return f'Junglist {res}'


panyo = Raver('Spasov')
print(panyo.say_my_name()) # Junglist Spasov
print(Raver.__mro__) # (<class '__main__.Raver'>, <class '__main__.Human'>, <class 'object'>), method resolution order (MRO) opitva da dostupva v sledniq red za metodi i atributi kato ierarhiq. class object e nasledqvan ot vseki klas
#
# # tozi primer e da pokaje 4e super() moje da se polzva v vsqkvi metodi, ne samo v __init__
#
# print(dir(object)) # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
