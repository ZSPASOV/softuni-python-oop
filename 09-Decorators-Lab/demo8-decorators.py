def uppercase(fn): # decorator
    def wrapper():
        result = fn()
        return result.upper()
    return wrapper()


def say_hi():
    return 'Hi!'

print(say_hi())
print(uppercase(say_hi)) # HI! # tova e dekorirane, wrap-vane na funkciqta
say_hi = uppercase(say_hi)
print(say_hi) # HI! - decoration. # pattern koito se izpolzva dosta chesto v programiraneto.
# podavane na call-able obekt na druga funckiq i tq da vurne wrapper, neshto koeto obgrushta dadena funkciq
# i promenq povedenieto i.

# v python moje i taka:

@uppercase # decoration
def say_hi():
    return 'Hi!'
print(say_hi)
