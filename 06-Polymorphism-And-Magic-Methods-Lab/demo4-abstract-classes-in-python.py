# Python, doesn't have true abstract classes and methods
# It can be achieved, but it is ugly
# tova e stariq nachin ot Python 2
class Shape:
    def __init__(self):
        if type(self) == Shape:
            raise TypeError('This is an abstract class')

    def area(self):
        raise TypeError('This is an abstract class')

    def perimeter(self):
        raise TypeError('This is an abstract class')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rect(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

circle = Circle(5)
print(circle.area()) # 78.5


square = Rect(5, 5)

def print_the_area(shape: Shape):
    print(shape.area())

print_the_area(square) # 25
print_the_area(circle) # 78.5
circle = Shape() # TypeError: This is an abstract class

# ideqta da se polzva base class e 4e imame ednakuv interface
# toest vsi4ki classes nqkva forma, primerno circle, square, vinagi shte imat funkciq area
# tq shte se iz4islqva po razli4en na4in, no vinagi shte ima funkciq area
# taka vseki class koito nasledqva Shape shte ima edni i sushti funkcii