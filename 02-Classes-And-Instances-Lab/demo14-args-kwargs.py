class Baba:
    def __init__(self, *args: tuple, **kwargs: dict):
        self.args = args
        self.kwargs = kwargs

    def print_args_and_kwargs(self):
        print(self.args, self.kwargs)


baba = Baba(1, 2, 3, 4, dqdo=42, grandson=55)
baba.print_args_and_kwargs() # (1, 2, 3, 4) {'dqdo': 42, 'grandson': 55}