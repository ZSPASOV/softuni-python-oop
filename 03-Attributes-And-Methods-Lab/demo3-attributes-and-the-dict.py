# A special attribute of every module is __dict__
# This is the dictionary containing the module's symbol table
# print(object.__dict__)

# A dictionary or other mapping object used to store an object's (writable) attributes

class MyClass(object):
    class_variable = 1

    def __init__(self, i_var):
        self.instance_variable = i_var

foo = MyClass(2)
bar = MyClass(3)

print(MyClass.__dict__) # {'{'__module__': '__main__', 'class_variable': 1, '__init__': <function MyClass.__init__ at 0x00000000026734C0>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}}
print(foo.__dict__)     # { 'instance_variable': 2 }
print(bar.__dict__)     # { 'instance_variable': 3}


# note - v samiq class vijdame class variable: 1 , za class-a tova e writable attribute
# v instanciite foo i bar vijdame instance_variable: 2 i instance_variable: 3, tova sa writable attributes za tezi instancii