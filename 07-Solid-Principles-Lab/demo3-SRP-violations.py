# SRP states that classes should have one responsibility. Here we have two:
    # student properties management
    # student database management

class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def register(self, student):
        pass
