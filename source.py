# LIBRARY MANAGEMENT SYSTEM
# Features:
# - Admin & Visitor login
# - Add Books (Admin only)
# - View Books
# - Borrow Books
# - Return Books + Fine (₹10/day after 14 days)
from datetime import datetime
# List to store all book details
all_books = []
# Add a new book (Admin only)
def add_book():
    print(" Add New Book")

    b_id = input("Enter Book ID: ")
    b_title = input("Enter Book Title: ")
    b_author = input("Enter Author Name: ")

    book_info = {"id": b_id, "title": b_title, "author": b_author,"is_free": True,"taken_on": None}
    all_books.append(book_info)
    print(f"Book '{b_title}' added successfully!")
# View all books
def show_books():
    print("Library Books")

    if not all_books:
        print("No books added yet.")
        return

    for bk in all_books:
        status = "Available" if bk["is_free"] else "Borrowed"

        print(f"\nID: {bk['id']}")
        print(f"Title: {bk['title']}")
        print(f"Author: {bk['author']}")
        print(f"Status: {status}")
# Borrow a book
def borrow_book():
    print("\n=== Borrow Book ===")
    bkid = input("Enter Book ID to borrow: ")

    for item in all_books:
        if item["id"] == bkid:
            if item["is_free"]:

                item["is_free"] = False
                item["taken_on"] = datetime.now()

                print(f"You borrowed '{item['title']}'. Enjoy reading!")
                return
            else:
                print("This book is already borrowed.")
                return

    print("Book not found.")
# Fine Calculation (₹10/day after 14 days)
def calc_fine(dt_borrowed):
    days_used = (datetime.now() - dt_borrowed).days

    if days_used <= 14:
        return 0

    extra_days = days_used - 14
    return extra_days * 10
# Return a book
def return_book():
    print("Return Book")
    bkid = input("Enter Book ID to return: ")

    for bk in all_books:
        if bk["id"] == bkid:
            if not bk["is_free"]:

                fine_here = calc_fine(bk["taken_on"])

                bk["is_free"] = True
                bk["taken_on"] = None

                print(f"Book '{bk['title']}' returned successfully!")

                if fine_here > 0:
                    print(f"Fine to be paid: ₹{fine_here}")
                else:
                    print("No fine. Thank you!")

                return
            else:
                print("This book was not borrowed.")
                return

    print("Book not found.")
# Login System (Admin / Visitor)
def login():
    print("\n=== LOGIN ===")
    print("1. Admin")
    print("2. Visitor")

    choice = input("Select user type: ")

    if choice == "1" or choice.lower() == "admin":
        pwd = input("Enter Admin Password: ")
        if pwd == "admin123":
            print("Admin Login Successful.")
            return "admin"
        else:
            print("Wrong password! Logged in as Visitor.")
            return "visitor"

    elif choice == "2":
        print("Logged in as Visitor.")
        return "visitor"

    else:
        print("Invalid choice! Logged in as Visitor.")
        return "visitor"
# Main Menu (changes based on user type)
def main_menu(user_type):
    while True:
        print("      LIBRARY MANAGEMENT")
        # Admin Menu
        if user_type == "admin":
            print("1. Add Book")
            print("2. View Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Exit")

        # Visitor Menu
        else:
            print("1. View Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Exit")

        choice = input("Enter your choice: ")

        # Admin Functions
        if user_type == "admin":
            if choice == "1":
                add_book()
            elif choice == "2":
                show_books()
            elif choice == "3":
                borrow_book()
            elif choice == "4":
                return_book()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

        # Visitor Functions
        else:
            if choice == "1":
                show_books()
            elif choice == "2":
                borrow_book()
            elif choice == "3":
                return_book()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")



user = login()
main_menu(user) create a readme.md
