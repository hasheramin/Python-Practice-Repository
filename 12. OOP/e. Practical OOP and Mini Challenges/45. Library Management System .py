# A Program to create a simple library management system

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_details(self):
        print(f"{self.title} by {self.author}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.show_details()


book1 = Book("Python Basics", "Hasher")
book2 = Book("Learning OOP", "Amin")

library = Library()

library.add_book(book1)
library.add_book(book2)

library.show_books()


# Explanation:
# Book represents an individual book with title and author.
# Library stores Book objects inside its books list.
# Books are created independently and then added to the Library.
# The library uses each Book object's show_details() method.

# Real-Life Use:
# This structure can be extended into a real library system with borrowing, returning, searching, and member management.