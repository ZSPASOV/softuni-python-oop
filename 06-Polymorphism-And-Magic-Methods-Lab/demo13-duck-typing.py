# "If it looks like a duck and quacks like a duck, it's a duck"
    # i.e. we don't care about objects' types, but whether they have the methods we need
# All len() cares about is whether the passed object has an override of the __len__ method
class MyClass:
    def __init__(self, size):
        self.size = size
    def __len__(self):
        return self.size


print(len("peter")) # 5
print(len([10, 20, 30])) # 3
print(len(MyClass(4))) # 4
print(len(MyClass(3))) # 3



