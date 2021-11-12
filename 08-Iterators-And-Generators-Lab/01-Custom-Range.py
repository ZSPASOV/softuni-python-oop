class custom_range: # imeto na klasa narushava konvenciqta, no taka go iska v judge v primera
    def __init__(self, start, end):
        self.index = start
        self.end = end

    def __iter__(self):
        return self # tuk suzdavame iterator, v sluchaq iteratora shte e samiq class custom_range, zatova davame return self

    def __next__(self):
        if self.index <= self.end:
            index = self.index
            self.index += 1
            return index
        raise StopIteration()


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
