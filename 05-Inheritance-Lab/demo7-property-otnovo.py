# v1 - na4ina za dostupvane na private attribute, s getter
# za setvane - sus setter
# tova go ima i v drugi obektno orientirani ezici

class Baba:
    def __init__(self):
        self.__a = 1

    def get_a(self):
        return self.__a


    def set_a(self, value):
        self.__a = value


baba = Baba()
print(baba.get_a()) # 1
baba.set_a(42)
print(baba.get_a()) # 42

# v2 - pythonic na4in za dostupvane na private attribute, s @property i s @var.setter

class Baba:
    def __init__(self):
        self.__a = 1

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value


baba = Baba()
print(baba.a) # 1 - taka dostupvaneto stava bez skobi, kato polzvame @property
baba.a = 42 # s @a.setter nqma nujda da izvikvame method
print(baba.a) # 42