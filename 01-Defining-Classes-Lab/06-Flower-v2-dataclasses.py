from dataclasses import dataclass


@dataclass # note - pri dataclass zadaljitelno trqbva da se polzva typehint sled ime na promenliva
class Flower:
    name: str
    water_requirements: int
    is_happy: bool = False

    def water(self, quantity):
        self.is_happy = quantity >= self.water_requirements # shte vurne bool stoinost True ili False

    def status(self):
        if self.is_happy:
            return f'{self.name} is happy'
        else:
            return f'{self.name} is not happy'

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
