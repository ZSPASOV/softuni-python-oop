# ne e za judge, prosto primer

def number_increment(n):
    def inner(fn):
        def wrapper(*args, **kwargs):
            res = fn(*args, **kwargs)
            return [i + n for i in res]
        return wrapper
    return inner


@number_increment(102)
def get_numbers():
    return [1, 2, 3, 4, 5]

print(get_numbers())