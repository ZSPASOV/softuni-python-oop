import random


class EndlessIterator:
    def __iter__(self):
        return self

    def __next__(self):
        i = random.randint(0, 100)
        if i == 42:
            raise StopIteration()
        return i


iterator = EndlessIterator()
for i in iterator:
    print(i)
# pokazva kak raboti raise StopIteration()