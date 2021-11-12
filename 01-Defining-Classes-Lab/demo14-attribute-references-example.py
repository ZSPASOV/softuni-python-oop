class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

# MyClass.i and MyClass.f are valid attribute references
# Class attributes can also be assigned, so you can change the value of MyClass.i by assignment

print(MyClass.i) # 12345
print(MyClass.f) # <function MyClass.f at 0x00000000026403A0>


# Class attributes can also be assigned, so you can change the value of MyClass.i by assignment

MyClass.i = 2

print(MyClass.i) # 2