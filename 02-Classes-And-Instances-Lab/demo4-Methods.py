# A method is a function that belongs to an object
# All attributes of a class that are function objects define corresponding methods of its instances
    #  valid method reference: x.say_hello
    #  invalid method reference: x.number

class MyClass:
    number = 743

    def say_hello(self):
        return 'Hello'

x = MyClass()
print(x.say_hello) # <bound method MyClass.say_hello of <__main__.MyClass object at 0x0000000000463790>>
print(x.say_hello()) # Hello