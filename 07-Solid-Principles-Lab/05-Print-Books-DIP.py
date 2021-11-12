# class Book:
#     def __init__(self, title, author, content: str):
#         self.title = title
#         self.author = author
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class AuthorFormatter:
#     def format(self, book: Book) -> str:
#         return book.author
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book
#
#     def get_author(self, book: Book):
#         formatter = AuthorFormatter()
#         return formatter.format(book)
#
#
# book = Book('Principles', 'Ray Dalio', 'Lorem ipsum dolor sit amet')
# printer = Printer()
# print(printer.get_book(book)) # Lorem ipsum dolor sit amet
# print(printer.get_author(book)) # Ray Dalio



# SOLID Refactoring :
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class ContentFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class AuthorFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.author


class Printer:
    def print(self, book: Book, formatter: Formatter):
        return formatter.format(book)


book = Book('Principles', 'Ray Dalio', 'Lorem ipsum dolor sit amet')
printer = Printer()
print(printer.print(book, ContentFormatter())) # Lorem ipsum dolor sit amet
print(printer.print(book, AuthorFormatter())) # Ray Dalio


