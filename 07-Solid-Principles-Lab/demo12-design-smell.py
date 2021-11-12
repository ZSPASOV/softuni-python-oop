# If the code is checking the type of class
# Overridden methods change their behaviour 
# Override a method of the superclass by an empty method
# Base class depends on its subtypes


def greeter(person: Person):
    if type(person) == Person: # code smell, violation of LSP
        raise TypeError('Expecting Person')
    return person.say_hi()


# pravilen na4in:

def greeter(person: Person):
    if not isinstance(person, Person):
        raise TypeError('Expecting Person')
    return person.say_hi()