from dto.book import Book
from dto.book_quantities import BookQuantity
from typing import Dict, List

class Catalog:

    def __init__(self) -> None:
        self.books: Dict[str, BookQuantity] = {}

    def add_book(self, book: Book, quantity: int) -> None:
        if book.title not in self.books:
            self.books[book.title] = BookQuantity(book, quantity)

    def borrow_book(self, book: Book) -> None:
        self.books[book.title].decrement_quantity()

    def return_book(self, book: Book) -> None:
        self.books[book.title].increment_quantity()

    def is_book_available(self, book: Book) -> bool:
        return book.title in self.books and self.books[book.title].quantity > 0

    def search_books(self, title: str, author: str, isbn: str, publication: str, year: int) -> List[Book]:
        books_available = []
        for book_quantity in self.books.values():
            if book_quantity.is_available():
                book = book_quantity.book
                if (title and title in book.title) or \
                        (author and author in book.author) or \
                         (isbn and isbn in book.isbn) or \
                          (publication and publication in book.publication) or \
                           (year and year == book.year):
                    books_available.append(book)
        return books_available

    def get_all_books(self) -> List[Book]:
        books_available = []
        for book_quantity in self.books.values():
            if book_quantity.is_available():
                books_available.append(book_quantity.book)
        return books_available