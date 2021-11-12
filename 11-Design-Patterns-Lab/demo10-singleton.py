# singleton pattern
class God:
    _instance = None

    def __init__(self):
        assert God._instance is None
        God._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            return cls()
        return cls._instance


god_of_peter = God.get_instance()
god_of_ivan = God.get_instance()

# edna i sushta instanciq.
print(god_of_peter) # <__main__.God object at 0x00000000024DB520>
print(god_of_ivan) # <__main__.God object at 0x00000000024DB520>