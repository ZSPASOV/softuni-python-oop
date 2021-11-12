class Person:
    def __init__(self):
        self.__name = 'baba'


    @property
    def name(self):
        return self.__name

person = Person()
print(person.name) # baba

