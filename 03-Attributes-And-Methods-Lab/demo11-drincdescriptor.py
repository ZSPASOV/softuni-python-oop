# primer izvan lekciq
class Drink:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class DrinksDescriptor:
    def __get__(self, *args):
        return [Drink('Whiskey'), Drink('Beer')]

    def __set__(self, *args):
        raise Exception('You cannot change our menu!')

class Bar:
    drinks = DrinksDescriptor()


bar = Bar()
print(bar.drinks)  # [Whiskey, Beer]