def dqdo():
    yield 42
    yield 43


gen = dqdo()
print(next(gen)) # 42
print(next(gen)) # 43
print(next(gen)) # StopIteration