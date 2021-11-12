class Baba:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def make_bob_chorba():
        print('Preparing bob chorba!')

baba = Baba('Test')
baba.make_bob_chorba()