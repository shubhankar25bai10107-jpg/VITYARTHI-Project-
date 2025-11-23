Here is the `README.md` for your Library Management System in Python.

````markdown
# 📚 Simple Library Management System (LMS)

This is a basic console-based Library Management System implemented in Python. It allows users to log in as an **Admin** or a **Visitor** and perform various library operations like viewing, borrowing, and returning books, with an automatic fine calculation system for late returns.

## ✨ Features

* **User Roles:** Separate login for **Admin** and **Visitor**.
* **Book Management (Admin Only):** Add new books to the library collection.
* **View Books:** Display all books, including their availability status.
* **Borrow Books:** Visitors can borrow available books.
* **Return Books & Fine System:** Calculate and apply a fine for books returned after the **14-day** due period.

## ⚙️ Fine Policy

* **Due Date:** 14 days from the borrowing date.
* **Fine Rate:** ₹10 per day for every day past the 14-day limit.

## 🚀 How to Run

1.  **Save the Code:** Save the Python code (provided in your prompt) as a file named `lms.py`.
2.  **Run from Terminal:** Open your terminal or command prompt and execute the script:

    ```bash
    python lms.py
    ```

3.  **Follow the Prompts:** The system will first prompt you to log in as an **Admin** or **Visitor**.

## 🔑 Login Details

| User Type | Password | Access Rights |
| :--- | :--- | :--- |
| **Admin** | `admin123` | Add Books, View Books, Borrow, Return |
| **Visitor** | (Any/None) | View Books, Borrow, Return |

## 💻 Code Structure

The system is built around several key functions:

| Function | Description | Access |
| :--- | :--- | :--- |
| `login()` | Handles user authentication and determines the user type (`admin` or `visitor`). | All |
| `add_book()` | Allows an Admin to input and add new book details. | Admin |
| `show_books()` | Displays the details and status of all books in the `all_books` list. | All |
| `borrow_book()`| Changes a book's status to borrowed and records the borrowing time. | All |
| `calc_fine(dt_borrowed)`| Calculates the fine based on the return date and the 14-day limit. | Internal |
| `return_book()`| Changes a book's status to available and displays any calculated fine. | All |
| `main_menu(user_type)`| Displays the appropriate menu options based on the logged-in user. | All |

## 🛠️ Dependencies

This system uses the built-in **`datetime`** module for managing borrowing and return times, which is necessary for the fine calculation. No external libraries are required.
````
