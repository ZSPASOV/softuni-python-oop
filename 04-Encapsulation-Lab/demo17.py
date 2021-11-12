class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        return self._temperature

    # setter
    def set_temperature(self, value):
        self._temperature = value


a = Celsius(37)

print(a.temperature)

a.set_temperature(40)
print(a.temperature)
print(a._temperature)

