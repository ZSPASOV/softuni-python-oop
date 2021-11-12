# otgovor na vapros ot slido
from abc import ABC, abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name


class SoundMakingAnimal(Animal, ABC): # moje da stane no mnojestvenoto nasledqvane ne e dobra ideq
    @abstractmethod
    def make_sound(self):
        pass
