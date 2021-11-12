class SomeClass:
    @classmethod
    def some_class_method(cls, value):
        pass

    @staticmethod
    def some_static_method():
        pass

SomeClass.some_class_method(50) # can be called by instance
SomeClass().some_class_method(0) # can be called by class

SomeClass.some_static_method() # can be called by instance
SomeClass().some_static_method() # can be called by class

# edinstvenata razlika mejdu classmetodite i stati4nite metodi e 4e:
# classmethod-ite priemat klasa kato parvi argument
