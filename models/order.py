from models.book import Book, BookManagement


class Cart:

    def __init__(self, user, books=None):
        self.user = user
        self.books = [books] or []

    def add_to_cart(self, book: Book):
        self.books.append(book)

    def __str__(self):
        return f"Cart for {self.books}"


class Order:
    def __init__(self, cart: Cart):
        self.cart = cart
        self.price = self.calculate_price()
        self.user = self.cart.user

    def calculate_price(self):
        total_price = sum([e.price for e in self.cart.books])
        return total_price

    def validate(self):
        books_counts = {}
        for book in self.cart.books:
            books_counts[book.name] = books_counts.get(book.name, 0) + 1
        for book in self.cart.books:
            if book.total_available < books_counts.get(book.name):
                raise Exception(f"Order can't be places because book {book.name} are/is not sufficient available")
        return True

    def place(self):
        for book in self.cart.books:
            BookManagement.remove_book(book.name)


def __str__(self):
    return f"Order for {self.user.username} and {self.cart} and price: {self.price}"
