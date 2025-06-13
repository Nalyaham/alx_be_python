class Book:
    def __init__(self, title, author, ):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def checked_out(self):
        return self.__is_checked_out

class Library:
    def __init__(self):
        self.__books = []

    def availability(self):
        return self.book.checked_out()

    def add_book(self, title):
        self.__books.append(title)

    def check_out_book(self, title):
        for book in self.__books:
            if title == self.__books and not library.availability:
                self.is_checked_out = True

    def return_book(self, title):
        for book in self.__books:
            if title == self.__books and library.availability:
                self.is_checked_out = False

    def list_available_books(self):
        for book in self.__books:
            if book.checked_out():
                print(self.__books)

library = Library()
Book("Brave New World", "Aldous Huxley")
Book("1984", "George Orwell")
