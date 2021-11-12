def multiply(n):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs) * n
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3)) # 39

# (6 + 10) * 5 = 80
@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6)) # 80