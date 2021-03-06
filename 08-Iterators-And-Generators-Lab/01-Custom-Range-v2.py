class CustomRangeIterator:
    def __init__(self, start, end):
        self.index = start
        self.end = end

    def __next__(self):
        if self.index <= self.end:
            index = self.index
            self.index += 1
            return index
        raise StopIteration()


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return CustomRangeIterator(self.start, self.end)




one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
