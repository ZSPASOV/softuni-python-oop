# Sometimes we might need to define a decorator that accepts arguments
# We achieve this by passing the arguments to the wrapper function
# The arguments will then be passed to the function that is being decorated at call time


from time import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(end - start)
        return result
    return wrapper
