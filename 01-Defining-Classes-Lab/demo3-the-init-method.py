# When a class defines an __init__() method, this method is invoked
# for the newly-created class instance

class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model

my_laptop = Laptop("Inspiron 15", "Dell")
