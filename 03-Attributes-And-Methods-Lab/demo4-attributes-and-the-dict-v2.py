class Baba:
    def __init__(self):
        self.a = 1
        self.b = 42

    def print_b(self):
        print(self.b)

baba = Baba()
print(baba.__dict__) # {'a': 1, 'b': 42}
baba.print_b() # 42
baba.__dict__['b'] = 43
baba.print_b() # 43