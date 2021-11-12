class Baba:
    def __init__(self, size):
        self.size = size


    def __add__(self, other):
        return self.size + other

baba = Baba(99)
print(baba + 42) # 141