# The Singleton pattern is used when we want to guarantee that only one instance of a given class exists during runtime
# The Singleton is considered an anti-pattern, because:
# It makes the code more complex and less useful
# It introduces unnecessary restrictions
# It is hard to test

def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper

@singleton
class DBConnection(object):

    def __init__(self):
        """Initialize your database connection here."""
        pass

    def __str__(self):
        return 'Database connection object'

a = DBConnection()
b = DBConnection()

