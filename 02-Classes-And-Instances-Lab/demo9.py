class Example:
    pass


example = Example()

def say_hi(self):
    print('saying hi')


Example.say_hi = say_hi

example.say_hi() # saying hi