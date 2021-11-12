class Baba:
    def make_bob_chorba(self):
        print('Making bob chorba.')


class Dqdo:
    def __init__(self, baba: Baba):
        self.baba = baba

    def drink_rakia(self):
        self.baba.make_bob_chorba()
        print('Drinking rakia!')


baba = Baba()
dqdo = Dqdo(baba)

dqdo.drink_rakia() # Making bob chorba.
                   # Drinking rakia!