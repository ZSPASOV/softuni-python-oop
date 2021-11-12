# To make Shape conform to the ISP principle, we segregate the actions to different classes
# Classes Circle and Rectangle can inherit from class Shape and implement their own draw behaviour
class Shape:
    def draw(self):
        raise NotImplementedError

class Rectangle(Shape):
    def draw(self):
        pass
class Circle(Shape):
    def draw(self):
        pass
