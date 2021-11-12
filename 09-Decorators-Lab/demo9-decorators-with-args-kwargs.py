def uppercase(function): # decorator
    # function: non-local for wrapper
    # function: local for uppercase
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        uppercase_result = result.upper()
        return uppercase_result
    return wrapper


@uppercase # decoration
def say_hi(name):
    return f'hello there {name}'

print(say_hi('Panyo')) # 'HELLO THERE PANYO'
