import dataclasses


@dataclasses.dataclass
class Baba:
    a: int   # instance-attribute
    b: int   # instance-attribute
    c = None # class-attribute


if __name__ == '__main__':
    baba = Baba(1, 2)
    print(baba.a) # 1
    print(baba.b) # 2

print(__name__) # __main__