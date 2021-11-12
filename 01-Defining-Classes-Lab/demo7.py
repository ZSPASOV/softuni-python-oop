class Person:
    def __init__(self, name):
        self.name = name

jordan = Person('Jordan')
savina = Person('Savina')

Person.say_hi = lambda self: f'Hi, my name is {self.name}'

print(jordan.say_hi()) # Hi, my name is Jordan.  taka shte proveri dali kum nashata instanciq ima zakachen metod, ako nqma shte proveri dali v klasa ima takav zaka4en metod

Person.say_bye = lambda self: f'Bye'
print(jordan.say_bye()) # Bye

jordan.say_bye = lambda self: f'Bye!'
jordan.say_bye() # TypeError: <lambda>() missing 1 required positional argument: 'self'

# nqma kak da ima metod zakachen kum instanciqta, trqbva da e zakachen kum class-a

