# Generators are a simple way of creating iterators
# A generator is a function that returns an object (iterator)
# This iterator can later be iterated over (one value at a time)

def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_first_n = sum(first_n(5))
print(sum_first_n) # 10
