class WeirdInt(int):
    def __gt__(self, other):
        return False


a = WeirdInt(42)
b = WeirdInt(43)

print(a > b) # False
print(b > a) # False

# taka proverihme povedenieto s koeto python proverqva dali neshto e po golqmo