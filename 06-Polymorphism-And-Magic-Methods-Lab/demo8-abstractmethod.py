# s @abstractmethod se izbira koi metodi sa zaduljitelni za implementaciq
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    def sound(self): # dobavqme zaduljitelniq method sound
        return 'Meow!'


    def eat(self):  # razshirqvame s dopalnitelna funkcionalnost eat
        return 'Eat'