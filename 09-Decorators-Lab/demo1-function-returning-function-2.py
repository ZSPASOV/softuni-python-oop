def hello_function():
    def say_hi():
        return "Hi"
    return say_hi()


print(hello_function()) # Hi


def hello_function_two():
    def say_hi():
        return "Hi"
    return say_hi


print(hello_function_two()) # <function hello_function_two.<locals>.say_hi at 0x0000000002676550>
print(hello_function_two()()) # Hi


