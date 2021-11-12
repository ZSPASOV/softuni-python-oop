# primer izvan lekciqta
class Drink:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Bar:
    @property
    def drinks(self):
        return [Drink('Whiskey'), Drink('Beer')]


bar = Bar()
print(bar.drinks) # [Whiskey, Beer]