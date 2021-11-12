# not a best practice but to show it works

class OrderBook:
    pass

OrderBook.__init__ = lambda self, a: print(a)
OrderBook.say_hi = lambda self: 'Hi!'

ob = OrderBook(42)
print(ob.say_hi())