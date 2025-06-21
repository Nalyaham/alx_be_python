class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, file_size):
        super().__init__(title, author)
        self.ba = float(page_count)

class PrintBook(Book):
    def __init__(self, page_count):
        super().__init__(title, author)
        self.ba = float(page_count)

class Library:
    def __init__(self, books):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        self.books()
