class MyClass:
    def __init__(self, size):
        self.size = size
    def __len__(self):
        return self.size


a = MyClass(3)

print(a.__len__()) # 3
print(len(a)) # 3