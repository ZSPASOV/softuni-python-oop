class Person:
    def __init__(self, age=0):
        self.__age = age # tova e editnato, v ppt e greshno

    @property
    def asd(self):
        return self.__age

    @asd.setter
    def set_age(self, asd):
        if asd < 18:
            self.__age = 18
        else:
            self.__age = asd

person = Person(25)
print(person.asd)	# 25
person.set_age = 10
print(person.asd)	# 18
person.set_age = 30
print(person.asd)	# 30
