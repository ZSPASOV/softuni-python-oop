# Create a function called play_instrument which will receive an instance
# of an instrument and will print it's play() method
from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass


def play_instrument(instrument: Instrument):
    return instrument.play()


class Guitar: # moje i class Guitar(Instrument)
    def play(self):
        print("playing the guitar")

guitar = Guitar()
play_instrument(guitar)


class Piano: # moje i class Piano(Instrument)
    def play(self):
        print("playing the piano")
piano = Piano()
play_instrument(piano)
