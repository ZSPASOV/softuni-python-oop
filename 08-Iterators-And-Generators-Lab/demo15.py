def generator():
    i = 1
    while True:
        yield i
        i += 1


iterator = generator()
for i in iterator: # shte vurti bezkraino +1
    print(i)