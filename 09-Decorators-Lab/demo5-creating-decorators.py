# In the example below we create a decorator function that converts a sentence to upper case
def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper

