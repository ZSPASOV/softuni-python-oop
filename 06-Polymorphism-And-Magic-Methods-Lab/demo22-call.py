class Executor:
    def __init__(self, fn, *args):
        self.fn = fn
        self.args = args

    def __call__(self):
        return self.fn(*self.args)


def say_hi_to(name):
    print(f'Zdrasti, {name}')


hi_executor = Executor(say_hi_to, 'Jordan')
hi_executor() # Zdrasti, Jordan

# 4rez __call__ instanciqta na obekta stava callable