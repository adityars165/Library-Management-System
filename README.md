# 📚 Library Management System

A role-based desktop application built using **Python (Tkinter)** and **MySQL** that allows users and administrators to manage library operations like adding books, issuing books, and handling user book requests.

---

## ✨ Features

### 👤 User Module
- ✅ **Register & Login** with email and password
- 📖 **Request Books** from available inventory
- 📚 *(Planned)* **View My Issued Books** and request history

### 🛠️ Admin Module
- ➕ **Add Books** with title, author, and ISBN
- ❌ **Delete Books** using Book ID
- 📥 **Issue Books** to users based on pending requests
- 📋 **View Issued Books** for administrative tracking

---

## 🛠️ Tech Stack

| Component      | Technology        |
|----------------|-------------------|
| Frontend       | Python, Tkinter   |
| Backend Logic  | Python Classes    |
| Database       | MySQL             |
| Connector      | `mysql.connector` |

---

## 🗂️ Folder Structure

.
├── gui.py # GUI layer with all interface windows
├── connector.py # Handles all MySQL DB operations
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🧪 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
2. Set Up MySQL Database
Create a database named library

Create these tables manually (or import SQL file if provided):

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
In connector.py, update:

python
Copy
Edit
user="your-mysql-username"
password="your-mysql-password"
4. Run the App
bash
Copy
Edit
python gui.py
