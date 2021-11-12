class Mouse:
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def move(self, x, y):
        for o in self.__observers:
            o.mouse_moved(x, y)


class Screen:
    def show(self):
        print('Rendering on display new position')

    def mouse_moved(self, x, y):
        print(f'New mouse position is {x}, {y}')
        self.show()


screen = Screen()
mouse = Mouse()
mouse.add_observer(screen)
mouse.move(50, 99)