# In order to achieve this, we define a decorator maker that accepts arguments
# Then we define a decorator inside it
# We then define a wrapper function inside the decorator as we did earlier
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(4)
def say_hi():
    print("Hello")

print(say_hi()) # Hello
                # Hello
                # Hello
                # Hello
                # None
