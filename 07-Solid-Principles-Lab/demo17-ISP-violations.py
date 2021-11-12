# Class Shape draws rectangle and circle
# Class Circle or Rectangle implementing the Shape class must define the methods draw_rectangle() and draw_circle()
class Shape:
    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError

# Class Rectangle implements method draw_circle it has no use of
# Class Circle implements method draw_rectangle

class Rectangle(Shape):
    def draw_rectangle(self):
        pass
    def draw_circle(self):
        pass

class Circle(Shape):
    def draw_rectangle(self):
        pass
    def draw_circle(self):
        pass
