class Baba:
    def __repr__(self):
        return 'baba'

    def introduce(self):
        return 'baba'

print(Baba()) # baba - s repr shte printira baba bez da izvikvame metoda, izvikva se implicitno
print(Baba().introduce()) # baba, trqbva da izvikame introduce za da printira baba, izvika se explicitno


a = Baba()
print(a)