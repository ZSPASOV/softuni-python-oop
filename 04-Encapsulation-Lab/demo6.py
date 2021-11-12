class BankAccount:
    def __init__(self, name, id, pin):
        self.name = name # public attribute
        self._id = id # protected attribute, moje da se dostupva oba4e ne e redno da se dostupva ili promenq 4rez publi4en interface
        self.__pin = pin # private attribute - dostupva se samo ot samiq klas i negovi instancii

    def get_pin(self): # getter method
        return self.__pin

    def set_pin(self, pin): # setter method
        self.__pin = pin

bank_account = BankAccount(123, 1234, 'Jordan Account')
print(bank_account._BankAccount__pin) # moje da go dostapvame, no ne e jelatelno, samo konvenciqta go pazi, v ezici kato java, c++ nqma kak da se dostupi private i protected izvan klasa
bank_account.set_pin(5123)
print(bank_account.get_pin()) # tova e pravilniq nachin