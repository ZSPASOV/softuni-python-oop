# However, Python provides a much easier way for us to apply decorators
# We simply use the @ symbol before the function we would like to decorate
def uppercase(function): # decorator
    # function: non-local for wrapper
    # function: local for uppercase
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result
    return wrapper


@uppercase # decoration
def say_hi():
    return 'hello there'

print(say_hi()) # 'HELLO THERE'
