# tva nqma da raboti  v judge, v novite versii na Python e
from dataclasses import dataclass # tva go ima sled python 3.7

# sakraten sintaksis

@dataclass
class Book:
    name: str
    author: str
    pages: int

book = Book('My Book', 'Me', 200)
print(book.name)

