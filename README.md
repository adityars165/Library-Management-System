# 📚 Library Management System

A role-based desktop application built using **Python (Tkinter)** and **MySQL** that enables users and administrators to manage core library operations such as adding books, issuing them, and requesting books efficiently.

---

## ✨ Features

### 👤 User Module
- ✅ Register and login using email and password
- 📖 Request books from available inventory
- 📚 *(Planned)* View issued books and request history

### 🛠️ Admin Module
- ➕ Add new books with title, author, and ISBN
- ❌ Delete books using Book ID
- 📥 Issue books to users based on pending requests
- 📋 View all issued books

---

## 🛠️ Tech Stack

| Layer         | Technology        |
|---------------|-------------------|
| Frontend      | Python (Tkinter)  |
| Backend Logic | Python OOP        |
| Database      | MySQL             |
| Connector     | `mysql.connector` |

---

## 🧪 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

2. Set Up MySQL Database
Create a MySQL database named library

Use the following SQL schema to create the required tables:

sql
Copy
Edit
CREATE DATABASE library;

CREATE TABLE book (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(255),
    book_name VARCHAR(255),
    author VARCHAR(255)
);

CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE request_book (
    user_id INT,
    book_id INT,
    user_name VARCHAR(255),
    book_name VARCHAR(255)
);

CREATE TABLE issued_book (
    user_id INT,
    book_id INT,
    user_name VARCHAR(255),
    book_name VARCHAR(255)
);

3. Configure DB Credentials
In connector.py, update your credentials:
user="your_mysql_username"
password="your_mysql_password"

4. Run the Application
python gui.py
