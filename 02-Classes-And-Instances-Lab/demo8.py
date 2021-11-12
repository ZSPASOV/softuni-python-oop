class Example:
    def say_hi(self):
        print(self)

example = Example()
print(example) # <__main__.Example object at 0x0000000002503790>
print(Example()) # <__main__.Example object at 0x0000000002453250>
example.say_hi() # <__main__.Example object at 0x0000000002453790>
print(type(example)) # <class '__main__.Example'>