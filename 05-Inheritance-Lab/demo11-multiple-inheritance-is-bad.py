# ne e dobra praktika da se polzva multiple inheritence
# v edin moment neshtata mogat da stanat trudni za prosledqvane
# po dobre e da se polzva kompoziciq vmesto mnojestveno nasledqvane
class GrandMotherTheMotherofFather:
    pass


class GrandMotherTheMotherOfMother:
    pass


class Father(GrandMotherTheMotherofFather):
    pass

class Mother(GrandMotherTheMotherOfMother):
    pass

# bad
class Son(Mother, Father):
    pass

print(Son.__mro__) # (<class '__main__.Son'>, <class '__main__.Mother'>, <class '__main__.GrandMotherTheMotherOfMother'>, <class '__main__.Father'>, <class '__main__.GrandMotherTheMotherofFather'>, <class 'object'>)
# taka raboti method resolution order pri multiple inheritance, purvo gleda Mother posle GrandMotherTheMotherOfMother
# tova e trudno za prosledqvane, zashtoto hvashta edin nasleden klas i proverqva vsi4ki niva nazad za nego
# chak kato proveri vsi4ko za mother shte zapo4ne da proverqva za father


# good
class Son:
    def __init__(self):
        self.mother = Mother()
        self.father = Father()