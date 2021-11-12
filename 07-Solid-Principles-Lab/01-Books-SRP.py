# Refactor the provided code, so there is a separate class called Library,
# which contains books and has a method called find_book(title) that returns
# the book with the given title. Remove the unnecessary code from the Book class.

# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page


# SOLID Refactoring :
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f'{self.title} by {self.author}'


class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book


the_godfather = Book('The Godfather', 'Mario Puzo')
principles = Book('Principles', 'Ray Dalio')

library = Library([the_godfather, principles])
print(library.find_book('Principles'))


