# Create two classes named Animal and Dog.
# Animal with a single public method eat() that returns: "eating…"
# Dog with a single public method bark() that returns: "barking…"
# Dog should inherit from Animal.

class Animal:
    def eat(self):
        return 'eating...'


class Dog(Animal):
    def bark(self):
        return 'barking...'

dog = Dog()
print(dog.eat())
print(dog.bark())
