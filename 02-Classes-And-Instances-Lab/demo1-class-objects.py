# Class objects support two kinds of operations:
#  attribute references – can be addressed with object.attribute_name
#  instantiation - class instantiation uses function notation

class Example:
    text = 'Hello'

Example.text # attribute reference
x = Example() # instantiation


a = Example.text
print(a) # Hello
print(type(a)) # <class 'str'>
print(x) # <__main__.Example object at 0x00000000024D3790>
