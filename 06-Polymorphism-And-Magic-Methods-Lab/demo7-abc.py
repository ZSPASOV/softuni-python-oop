from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass




class Circle(Shape):
    pass


#circle = Circle() # TypeError: Can't instantiate abstract class Circle with abstract methods area

# v sluchaq abstractmethod-a shte vdiga greshka, koqto e kato reminder che nujniq method ne e suzdaden v Circle



# tova e pravilnoto
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius * self.radius


circle = Circle(20)

print(circle.area()) # 1256.0

