VOWELS = {'A', 'E', 'I', 'O', 'U'}


def vowel_filter(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [c for c in result if c.upper() in VOWELS]
    return wrapper


def make_upper(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [c.upper() for c in result]
    return wrapper

@vowel_filter
@make_upper
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters()) # ['A', 'E']

# dva dekoratora, filtrira glasni i gi pravi glavni bukvi