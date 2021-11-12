class Person:
    def __init__(self, name, father=None, mother=None):
        self.name = name
        self.father = father
        self.mother = mother


father = Person('Ivan')
mother = Person('Ivana')
son = Person('Ivancho', father=father, mother=mother)

# tova e eleganten variant vmesto multiple inheritance