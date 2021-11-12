class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()

print(x.f()) # 'hello world'
print(x.i) # 12345

# Creates a new instance of the class and assigns this object to the local variable x
# The instantiation operation creates an empty object
# Many classes create objects with instances customized to a specific initial state
# Therefore a class may define a special method named __init__()

