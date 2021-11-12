# We create two classes: Cat and Dog
# They will both have function called sound() that will print different strings depending on the animal
# We can create a method that calls the sound method, no matter of what the animal is
class Cat:
    def sound(self):
        print("Meow!")

class Dog:
    def sound(self):
        print("Woof woof!")


def makeSound(animalType): # works for both classes
    animalType.sound()

catObj = Cat()
dogObj = Dog()
makeSound(catObj) # "Meow!"
makeSound(dogObj) # "Woof woof!"
