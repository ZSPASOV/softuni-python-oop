a = 42

class Baba:
    a = 1 # class scope
    b = a + 1

print(Baba.b)  # 2

class Dqdo:
    b = a + 1

print(Dqdo.b) # 43 - tova e zashtoto interpretatora purvo tursi v class cope na class Dqdo, ne namira promenliva a
            # sled tova tursi v globalniq scope i tam ima a i vzima a = 42

class Son:
    a = 1
    b = a + 1

    def say_hi(self):
        print(a)

son = Son()
print(son.say_hi()) # 42, shte printne a = 42 ot globalniq scope, vupreki che ima a = 1 v lokalniq class scope.
                    # class scope sushtestvuva mnogo kratko, samo pri suzdavane na classa, posle v metodite vinagi tursi direktno globalniq scope