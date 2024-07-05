from collections import Counter, defaultdict

from models.book import BookManagement
from models.order import Order, Cart
from models.user import UserManagerObj


class OrderManagement:
    def __init__(self):
        self.orders: list[Order] = []
        self.cart_dict = {}

    def add_to_cart(self, username, book_name):
        user = UserManagerObj.get_a_user_with_username(username)
        if not user:
            raise Exception("User does not exist")
        book = BookManagement.get_a_book(book_name)
        if not book:
            raise Exception("book does not exist")
        if user.username in self.cart_dict:
            cart = self.cart_dict[user.username]
            cart.add_to_cart(book)
        else:
            cart = Cart(user, book)
            self.cart_dict[user.username] = cart
        return cart

    def order(self, username: str):
        cart = self.cart_dict.get(username)

        if cart:
            order = Order(cart)
            if order.validate():
                order.place()
                del self.cart_dict[username]
                print(
                    f"oder has placed for value : {order.price} "
                    f"for {username} for books: {[e for e in order.cart.books]}"
                )
        else:
            raise Exception(f"No cart for the user {username}")

    def display(self):
        for order in self.orders:
            print(order)


OrderManagementObj = OrderManagement()
