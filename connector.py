import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore
from tkinter import messagebox

class Connector_sql():

    def establish_connection(self):
        
        self.connection = mysql.connector.connect(
            host="localhost",      # Your MySQL server host (e.g., "localhost")
            user="",           # Your MySQL username (e.g., "root")
            password=""    # Your MySQL password
        )
        self.cursor = self.connection.cursor()
        return self.connection,self.cursor
        
        

    def add_book_to_db(self,isbn,book_name,author):
        connection,cursor = self.establish_connection(self)
        cursor.execute(f"INSERT INTO library.book VALUES (NULL,%s,%s,%s)",(isbn,book_name,author))
        self.connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Sucess","Book Added")

    
    def show_available_book(self):
        connection,cursor = self.establish_connection(self)
        cursor.execute(f"SELECT book_id,isbn,book_name FROM library.book")
        book_data = cursor.fetchall()
        cursor.close()
        connection.close()
        return book_data
    
    def show_available_book1(self):
        connection,cursor = self.establish_connection(self)
        cursor.execute(f"SELECT book_id,book_name FROM library.book")
        book_data = cursor.fetchall()
        cursor.close()
        connection.close()
        return book_data
    
    def delete_book(self,book_id,window):
        connection,cursor = self.establish_connection(self)
        cursor.execute(f"DELETE FROM library.book WHERE book_id = {book_id}",)
        self.connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Sucess","Book Deleted")

    def request_book(self):
        connection,cursor = self.establish_connection(self)
        cursor.execute(f"SELECT user_id,book_id,user_name,book_name FROM library.request_book")
        book_data = cursor.fetchall()
        cursor.close()
        connection.close()
        return book_data
    
    def issue_book(self,value):
        connection,cursor = self.establish_connection(self)
        cursor.execute(f"INSERT INTO library.issued_book VALUES(%s,%s,%s,%s)",value)
        self.connection.commit()
        cursor.execute(f"DELETE FROM library.request_book WHERE user_id = {value[0]} AND book_id = {value[1]}")
        self.connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Sucess","Book Issued")

    def user_register(self,fname,lname,email,password):
        connection,cursor = self.establish_connection(self)
        cursor.execute(f"INSERT INTO library.user (fname,lname,email,password) VALUES(%s,%s,%s,%s)",(fname,lname,email,password))
        self.connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Sucess","Registered, Now Login!")

    def user_login(self,email,password):
        connection,cursor = self.establish_connection(self)
        cursor.execute(f"SELECT email,password FROM library.user")
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        isLogin = False
        for i in data:
            if i[0] == email and i[1] == password:
                isLogin = True
                break

        if isLogin:
            return True
        else:
            return False
        
    def user_request_book(self,value,email):
        connection,cursor = self.establish_connection(self)
        cursor.execute(f"SELECT user_id,fname,lname FROM library.user WHERE email = %s",(email,))
        user_id,fname,lname = cursor.fetchall()[0]
        cursor.execute(f"INSERT INTO library.request_book (user_id,user_name,book_id,book_name) VALUES(%s,%s,%s,%s)",(user_id,f"{fname+"  "+lname}",value[0],value[1]))
        self.connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Sucess","Book Requested")

    def display_issued_book(self):
        connection,cursor = self.establish_connection(self)
        cursor.execute(f"SELECT user_id,book_id,user_name,book_name FROM library.issued_book")
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return data


        
        

obj = Connector_sql()
obj.establish_connection