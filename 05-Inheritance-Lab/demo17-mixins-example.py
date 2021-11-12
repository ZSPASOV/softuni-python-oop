class Vehicle:
    def __init__(self, position):
        self.position = position

    def travel(self, destination):
        pass

class Car(Vehicle):
    pass

class Clock():
    pass


class RadioMixin():
   def play_song_on_station(self, station_frequency):
       return f'playing song on radio frequency {station_frequency}'

class Car(Vehicle, RadioMixin):
    pass

class Clock(RadioMixin):
    pass


car = Car('Sofia')
clock = Clock()
print(car.play_song_on_station(95.0))	# playing song on radio frequency 95.0
print(clock.play_song_on_station(100.3))	# playing song on radio frequency 100.3


# If the base class doesn't define any of the variables that the mixins defines,
# we can use both codes below and get similar results
# If you inherit multiple mixins to your class, it is important to remember the
# order which Python inherits these parents: make the highest to lowest from left to right

class Car(Vehicle, RadioMixin):
    pass

class Car(RadioMixin, Vehicle):
    pass
