s = 'baba'
print((dir(s))) # shte pokaje vsichki atributi dostapni za nashata instanciq s

# ima dunder atributi i metodi

print((type(s))) # <class 'str'> s e instanciq na klas str

print((s.__dir__)) # <built-in method __dir__ of str object at 0x000000000267EBB0>

print(s.__dir__())