from models.book import BookManagement
from models.user import UserManagerObj
from order_management import OrderManagementObj

if __name__ == '__main__':
    # add to book to inventory
    BookManagement.register("book1", "auther 1", 2021, 12, 1)
    BookManagement.register("book2", "auther 2", 2021, 1, 2)
    BookManagement.register("book3", "auther 3", 2021, 2, 1)
    BookManagement.register("book4", "auther 4", 2021, 9, 4)
    BookManagement.display()
    # register users
    UserManagerObj.register("username1", "user1", "1999-04-12")
    UserManagerObj.register("username2", "user2", "1999-05-20")
    UserManagerObj.register("username3", "user3", "1999-06-2")
    UserManagerObj.register("username4", "user4", "1990-04-1")
    UserManagerObj.display()

    # Add to cart
    OrderManagementObj.add_to_cart("username1", "book1")
    OrderManagementObj.add_to_cart("username1", "book2")
    OrderManagementObj.order("username1")
    OrderManagementObj.display()

    try:
        # duplicate book
        BookManagement.register("book1", "auther 1", 2021, 12, 1)
    except Exception as e:
        # Book is already registered
        print(e)

    try:
        # -ve value
        BookManagement.register("book5", "auther 1", 2020, -1, 1)
    except Exception as e:
        # Price/total_available/total_book can't be negative
        print(e)

    try:
        # Invalid Year
        BookManagement.register("book5", "auther 1", -2020, 1, 1)
    except Exception as e:
        # Invalid Year
        print(e)

    try:
        # Invalid Year
        OrderManagementObj.add_to_cart("username2", "book1")
        OrderManagementObj.order("username2")
    except Exception as e:
        # Order can't be places because book book1 are/is not sufficient available
        print(e)

    try:
        # no cart
        OrderManagementObj.order("username3")
    except Exception as e:
        # No cart for the user username3
        print(e)
