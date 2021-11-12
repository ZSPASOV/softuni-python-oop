class Animal:
    def __init__(self):
        self.__a = 1 # private
        self._b = 2 # protected

    def eat(self):
        return 'eating...'


class Dog(Animal):
    def bark(self):
        return 'barking...'

    def get_b(self):
        return self._b

    def get_a(self):
        return self.__a

dog = Dog()
print(dog.get_b()) # 2 protected attribute se nasledqva
print(dog.get_a()) # AttributeError: 'Dog' object has no attribute '_Dog__a', private attribute ne se nasledqva
