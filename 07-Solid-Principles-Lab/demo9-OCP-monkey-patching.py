# Jambazov go pokazva no ne se preporu4va
# tva e dinami4no zaka4vane kum class na daden metod

class Book:
    def get_page(self):
        return 43

old_get_page = Book.get_page

Book.get_page = lambda self: 42
book = Book()
print(book.get_page()) # 42

Book.get_page = old_get_page
print(book.get_page()) # 43

# izpolzva se kogato iskate vremenno da promenite daden metod bez da pravite nov class
# tova e losha praktika