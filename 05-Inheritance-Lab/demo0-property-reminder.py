# pripomnqne kvo e property
class Baba:
    @property
    def a(self):
        return 42

    @a.setter
    def a(self, value):
        return None

baba = Baba()
baba.a = 43
print(baba.a) # 42 # prodaljava da e 42, taka polzvame property i za encapsulation

# property obrushta method v attribute