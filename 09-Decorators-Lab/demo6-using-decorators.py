# Our decorator function takes a function as an argument, so let us define a function and pass it to our decorator
# We learned earlier that we could assign a function to a variable
# We'll use that trick to call our decorator function

def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


def say_hi():
    return 'hello there'

decorate = uppercase(say_hi)
print(decorate()) # HELLO THERE
