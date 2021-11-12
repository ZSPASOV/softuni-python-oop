from functools import reduce

def some_fn(a, b):
    return a + b

print(reduce(some_fn, [1, 2, 3, 4, 5, 6]))