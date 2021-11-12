# A function can also generate another function
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
print(hello) # <function hello_function.<locals>.say_hi at 0x00000000026744C0>
print(hello()) # Hi




print(hello_function) # <function hello_function at 0x00000000026763A0>
print(hello_function()) # <function hello_function.<locals>.say_hi at 0x00000000026964C0>
print(hello_function()()) # Hi




# da pro4eta za higher order functions

def exec(fn):
    return fn()

hello = hello_function()
print(exec(hello)) # Hi
