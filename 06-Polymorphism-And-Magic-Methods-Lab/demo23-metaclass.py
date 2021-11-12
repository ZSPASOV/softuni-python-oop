# tova e dopalnitelen vapros izvan lekciqta, za po naprednali e

class Meta:
    def __new__(cls):
        res = object.__new__(cls)
        res.dqdo = 42
        return res


class Baba(metaclass=Meta):
    def __init__(self):
        pass

baba = Baba()
print(baba.dqdo)