from itertools import chain

print(chain([1, 2, 3, 4, 5], [6, 7, 8])) # <itertools.chain object at 0x00000000026283A0>

g = chain([1, 2, 3, 4, 5], [6, 7, 8])


for i in (g):
    print(i)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
