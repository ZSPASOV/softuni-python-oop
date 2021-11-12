class Account:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError('Cannot set negative balance')
        self.__balance = value


account = Account()
account.balance = -50 # ValueError: Cannot set negative balance