def generator():
    while True:
        yield 42


iterator = generator()
print(next(iterator)) # 42
print(next(iterator)) # 42