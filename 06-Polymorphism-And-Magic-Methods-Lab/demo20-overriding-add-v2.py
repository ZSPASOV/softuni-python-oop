class Baba:
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return f'Baba of size {self.size}'


    def __add__(self, other):
        return Baba(self.size + other.size)


baba_1 = Baba(99)
baba_2 = Baba(101)

print(baba_1 + baba_2) # Baba of size 200