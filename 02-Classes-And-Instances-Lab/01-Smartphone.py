class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps: list = []
        self.is_on: bool = False

    def power(self):
        if self.is_on == False:
            self.is_on = True
        elif self.is_on == True:
            self.is_on = False

    def install(self, app: str, app_memory: int):
        self.app = app
        self.app_memory = app_memory
        if self.memory >= self.app_memory and self.is_on == True:
            self.apps.append(self.app)
            self.memory -= self.app_memory
            return f'Installing {self.app}'
        elif self.memory >= self.app_memory and self.is_on == False:
            return f'Turn on your phone to install {self.app}'
        elif self.memory < self.app_memory:
            return f'Not enough memory to install {self.app}'

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
