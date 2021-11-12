def adder():
    i = 0

    def add(): # closure
        nonlocal i
        i += 1

    def get():
        return i

    return add, get


add, get = adder()
# add()
# add()
# add()
# print(get()) # 3




