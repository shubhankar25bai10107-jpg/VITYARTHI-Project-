# 📜 Project Statement

## Project Title

**Simple Library Management System (LMS) - Console Application**

## I. Project Purpose

This project implements a basic, standalone Library Management System designed to simulate core library operations in a command-line interface environment.

The primary goals are:
1.  To provide functional separation between administrative tasks (adding books) and general user tasks (borrowing, returning, viewing).
2.  To demonstrate the use of Python data structures (lists of dictionaries) for data storage.
3.  To implement time-based logic using the `datetime` module for calculating financial penalties (fines).

## II. Scope of the System

This system is a **proof-of-concept** and operates within the following constraints:

* **Data Persistence:** Data is stored in memory (`all_books` list) and is **not** saved to a file or database. All data will be lost when the application is closed.
* **User Management:** Only two roles are supported (`Admin` and `Visitor`) with a hardcoded Admin password. No registration or unique user tracking (beyond the general Visitor role) is implemented.
* **Book Tracking:** The system tracks whether a book is free/borrowed, and when it was taken, but does not track *who* borrowed the book.

## III. Fine Calculation Formula

The late return fine is calculated based on the following formula:

* **Grace Period:** $T_{grace} = 14$ days
* **Daily Fine Rate:** $R_{fine} = ₹10$
* **Days Borrowed:** $D_{used}$ (Calculated as $T_{return} - T_{borrow}$)

The fine amount ($\text{Fine}$) is calculated as:

$$\text{Fine} = \begin{cases} 0 & \text{if } D_{used} \le T_{grace} \\ (D_{used} - T_{grace}) \times R_{fine} & \text{if } D_{used} > T_{grace} \end{cases}$$

## IV. Technical Implementation Notes

The system relies on the following key Python components:
* The `datetime` object from the standard library for time recording and comparison.
* A global `all_books` list where each book is represented as a dictionary.

## V. License

This project is released under the **MIT License**.

*(A full copy of the license is available in the `LICENSE.md` file.)*
