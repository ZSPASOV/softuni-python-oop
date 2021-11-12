def generator():
    print('before 1')
    yield 1
    print('before 2')
    yield 2
    print('before 3')
    yield 3


iterator = generator()
for i in iterator:
    print(i)