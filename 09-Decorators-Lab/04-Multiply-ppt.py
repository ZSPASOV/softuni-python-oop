def multiply(times):
    def decorator(function):
        def wrapper(params):
            return times * function(params)
        return wrapper
    return decorator


# First we add 3 to 10 = 13 and then we multiply the result by 3: 13 * 3 = 39
@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3)) # 39

# (6 + 10) * 5 = 80
@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6)) # 80
