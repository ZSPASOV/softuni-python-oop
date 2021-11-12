from abc import ABC, abstractmethod

class Animal(ABC): # Defining an Abstract Class
    def __init__(self, name):
        self.name = name

    @abstractmethod # Decorator function that makes a method abstract
    def sound(self):
        raise NotImplementedError("Subclass must implement")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Bark!")


class Cat(Animal): # Inherit the Abstract Class
    def __init__(self, name):
        super().__init__(name)

    def sound(self): # Implement the Abstract method
        print("Meow!")


cat = Cat("Willy")
cat.sound() # Meow!
dog = Dog("Willy")
dog.sound() # Bark!
#animal = Animal("Willy") # TypeError: Can't instantiate abstract class Animal with abstract methods sound
# animal.sound()
# Meow!
# Bark!
# Error!
