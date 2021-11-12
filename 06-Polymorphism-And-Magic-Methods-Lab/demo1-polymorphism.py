# Polymorphism is based on the Greek words Poly (many) and morphism (forms)
# In software engineering, polymorphism means the usage of an objects though the interface of their base class
# i.e. Circle inherits Shape, so a circle instance can be used from an instance of type Shape

# Circle inherits Shape
class Circle(Shape):
    def __init__(self,radius):
        # implementation
    def area(self):
        # implementation
    def perimeter(self):
        # implementation

# print_shape expects a Shape object
def print_shape(s: Shape):
    print(f'Perimeter: {s.perimeter()}')
    print(f'Area: {s.area()}')

# Call print_shape with a Circle object
# print_shape(Circle(3))