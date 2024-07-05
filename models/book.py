from dataclasses import dataclass, Field
from datetime import datetime


@dataclass(unsafe_hash=True)
class Book:
    name: str
    auther: str
    published_year: int
    total_available: int
    total_book: int
    price: float


class BookStore:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.available_books: set[Book] = set()

    def register(self,
                 name: str,
                 auther: str,
                 published_year: int,
                 price: float,
                 total_book: int = 0):
        if name in self.books:
            raise Exception("Book is already registered")
        total_available = total_book
        if price < 0 or total_available < 0 or total_book < 0:
            raise Exception("Price/total_available/total_book can't be negative")
        if published_year < 0 or published_year > datetime.now().year:
            raise Exception("Invalid Year")
        new_book = Book(name, auther, published_year, total_available, total_book, price)
        self.books[new_book.name] = new_book
        if total_book > 0:
            self.available_books.add(new_book)

    def add_book(self, book_name: str, quantity: int = 1):
        if quantity < 1:
            raise Exception("Book quantity can't be less then 1")
        if book_name not in self.books:
            raise Exception(f"Book did not found {book_name}")
        book = self.books[book_name]
        book.total_book += quantity
        book.total_available += quantity
        self.available_books.add(book)
        return book.total_available

    def remove_book(self, book_name: str, quantity: int = 1):
        if quantity < 1:
            raise Exception("Book quantity can't be less then 1")
        if book_name not in self.books:
            raise Exception(f"Book did not found {book_name}")
        book = self.books[book_name]
        if book.total_available < quantity:
            raise Exception(
                f"You can't remove {quantity} book(s) because available books is/are {book.total_available}"
            )
        book.total_available -= quantity
        if book.total_available <= 0 and book in self.available_books:
            self.available_books.remove(book)
        return book.total_available

    def get_a_book(self, book_name: str):
        return self.books.get(book_name)

    def display(self):
        for book in self.available_books:
            print(book)


BookManagement = BookStore()
