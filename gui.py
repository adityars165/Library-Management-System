from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from connector import Connector_sql as cn

class App():

    def create_window(self,root,title):

        self.root = root
        self.root.title(title)
        self.root.geometry("1920x1080")
        self.root.config(bg='powderblue')


    def change_window(self,delete_window,new_window):

        delete_window.destroy()
        new_window()


    def homepage(self):

        homepage_window = Tk()
        self.create_window(homepage_window,"Library Management System")

        title = Label(homepage_window, text="Home Page", bg="powderblue", font=('Times New Roman',80,'bold'))
        title.place(anchor='center',relx='0.5',rely='0.25')

        admin_button = Button(homepage_window, text='Admin',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(homepage_window,self.admin_page))
        admin_button.place(relx=0.5,rely=0.55,x=-175,anchor='center',width=250)

        user_button = Button(homepage_window,text='User',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(homepage_window,self.user_login_register))
        user_button.place(relx=0.5,rely=0.55,x=185,anchor='center',width=250)
        
        homepage_window.mainloop()


    def admin_page(self):

        admin_window = Tk()
        self.create_window(admin_window,"Admin Page")

        title = Label(admin_window, text="Admin Page", bg="powderblue", font=('Times New Roman',80,'bold'))
        title.place(anchor='center',relx='0.5',rely='0.25')

        add_book_button = Button(admin_window, text='Add Book',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(admin_window,self.add_book))
        add_book_button.place(relx=0.5,rely=0.5,x=-600,anchor='center',width=250)

        delete_book_button = Button(admin_window, text='Delete Book',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(admin_window,self.delete_book))
        delete_book_button.place(relx=0.5,rely=0.5,x=-300,anchor='center',width=250)

        issue_book_button = Button(admin_window, text='Issue Book',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(admin_window,self.issue_book))
        issue_book_button.place(relx=0.5,rely=0.5,x=0,anchor='center',width=250)

        display_issued_book_button = Button(admin_window, text='Display Issued Book',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(admin_window,self.display_issued_book))
        display_issued_book_button.place(relx=0.5,rely=0.5,x=300,anchor='center',width=250)

        homepage_button = Button(admin_window, text='Home Page',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(admin_window,self.homepage))
        homepage_button.place(relx=0.5,rely=0.5,x=600,anchor='center',width=250)

        admin_window.mainloop()


    def user_login_register(self):

        user_login_register_window = Tk()
        self.create_window(user_login_register_window,"User Page")

        title = Label(user_login_register_window, text="Login / Register", bg="powderblue", font=('Times New Roman',80,'bold'))
        title.place(anchor='center',relx='0.5',rely='0.25')

        login_button = Button(user_login_register_window, text='Login',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(user_login_register_window,self.user_login))
        login_button.place(relx=0.5,rely=0.5,x=-300,anchor='center',width=250)

        register_button = Button(user_login_register_window,text='Register',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(user_login_register_window,self.user_register))
        register_button.place(relx=0.5,rely=0.5,x=0,anchor='center',width=250)

        homepage_button = Button(user_login_register_window, text='Home Page',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(user_login_register_window,self.homepage))
        homepage_button.place(relx=0.5,rely=0.5,x=300,anchor='center',width=250)
        
        user_login_register_window.mainloop()


    def user_login(self):
        user_login_window = Tk()
        self.create_window(user_login_window, "User Login")

        title = Label(user_login_window, text="Login", bg="powderblue", font=('Times New Roman', 80, 'bold'))
        title.place(anchor='center', relx='0.5', rely='0.21')

        # User ID Label and Entry
        user_id_label = Label(user_login_window, text="Email ID:", bg="powderblue", font=('Times New Roman', 20))
        user_id_label.place(relx=0.2, rely=0.45, anchor='center')
        user_id_entry = Entry(user_login_window, font=('Times New Roman', 20))
        user_id_entry.place(relx=0.35, rely=0.45, anchor='center', width=300)

        # Password Label and Entry
        password_label = Label(user_login_window, text="Password:", bg="powderblue", font=('Times New Roman', 20))
        password_label.place(relx=0.6, rely=0.45, anchor='center')
        password_entry = Entry(user_login_window, font=('Times New Roman', 20), show='*')
        password_entry.place(relx=0.75, rely=0.45, anchor='center', width=300)

        # Login Button
        login_button = Button(user_login_window, text='Login', font=('Times New Roman', 20, 'bold'),command=lambda:self.on_login(user_id_entry.get(),password_entry.get(),user_login_window))
        login_button.place(relx=0.5, rely=0.6, anchor='center', width=250)

        # Register Button
        register_button = Button(user_login_window, text='Login / Register', font=('Times New Roman', 20, 'bold'), 
                                command=lambda: self.change_window(user_login_window,self.user_login_register))
        register_button.place(relx=0.5, rely=0.7, anchor='center', width=250)

        user_login_window.mainloop()


    def on_login(self,email,password,window):
        self.email = email
        login = cn.user_login(cn,email,password)
        if login:
            self.change_window(window,self.on_user_login_page)
        else:
            messagebox.showinfo("Error","Invail Email Id or Password")

    def on_user_login_page(self):
        on_user_login_window = Tk()
        self.create_window(on_user_login_window, "User Login")

        title = Label(on_user_login_window, text="Welcome", bg="powderblue", font=('Times New Roman', 80, 'bold'))
        title.place(anchor='center', relx='0.5', rely='0.12')

        request_book_button = Button(on_user_login_window, text='Request a Book',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(on_user_login_window,self.user_request_book))
        request_book_button.place(relx=0.5,rely=0.5,x=-150,anchor='center',width=250)

        my_book_button = Button(on_user_login_window,text='My Books',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(on_user_login_window,self.user_login_register))
        my_book_button.place(relx=0.5,rely=0.5,x=150,anchor='center',width=250)

        back_button = Button(on_user_login_window, text='Back', font=('Times New Roman', 20, 'bold'), 
                            command=lambda: self.change_window(on_user_login_window, self.user_page))
        back_button.place(relx=0.5, rely=0.8, anchor='center', width=250)

        on_user_login_window.mainloop()

    
    def user_request_book(self):
        display_issued_book_window = Tk()
        self.create_window(display_issued_book_window, "Delete Book")

        title = Label(display_issued_book_window, text="Issue Book", bg="powderblue", font=('Times New Roman', 80, 'bold'))
        title.place(anchor='center', relx='0.5', rely='0.12')

        book_data = cn.show_available_book1(cn)
        style = ttk.Style()

        style.configure("Treeview", background="powderblue", fieldbackground="powderblue", foreground="black", font=("Arial", 10))
        columns = ("Book Id", "Book Name")

        tree = ttk.Treeview(display_issued_book_window, columns=columns, show="headings")
        tree.heading("Book Id", text="Book Id")
        tree.heading("Book Name", text="Book Name")

        tree.column("Book Id", width=100)
        tree.column("Book Name", width=250)


        for book in book_data:
            tree.insert('', END, values=book)

        tree.place(relx=0.5, rely=0.5, anchor='center')

        request_book_button = Button(display_issued_book_window, text='Request Book', font=('Times New Roman', 20, 'bold'), 
                            command=lambda:cn.user_request_book(cn,tree.item(tree.selection())['values'],self.email) )
        request_book_button.place(relx=0.4, rely=0.8, anchor='center', width=250)

        back_button = Button(display_issued_book_window, text='Back', font=('Times New Roman', 20, 'bold'), 
                            command=lambda: self.change_window(display_issued_book_window, self.on_user_login_page))
        back_button.place(relx=0.6, rely=0.8, anchor='center', width=250)

        display_issued_book_window.mainloop()
        
        

    def user_register(self):
        user_register_window = Tk()
        self.create_window(user_register_window, "User Login")

        title = Label(user_register_window, text="Register", bg="powderblue", font=('Times New Roman', 80, 'bold'))
        title.place(anchor='center', relx='0.5', rely='0.12')

        # User ID Label and Entry
        first_name_label = Label(user_register_window, text="First Name:", bg="powderblue", font=('Times New Roman', 20))
        first_name_label.place(relx=0.2, rely=0.35, anchor='center')
        first_name_entry = Entry(user_register_window, font=('Times New Roman', 20))
        first_name_entry.place(relx=0.35, rely=0.35, anchor='center', width=300)

        # Password Label and Entry
        last_name_label = Label(user_register_window, text="Last Name:", bg="powderblue", font=('Times New Roman', 20))
        last_name_label.place(relx=0.6, rely=0.35, anchor='center')
        last_name_entry = Entry(user_register_window, font=('Times New Roman', 20))
        last_name_entry.place(relx=0.75, rely=0.35, anchor='center', width=300)

        email_label = Label(user_register_window, text="Email:", bg="powderblue", font=('Times New Roman', 20))
        email_label.place(relx=0.2, rely=0.45,x=-30, anchor='center')
        email_entry = Entry(user_register_window, font=('Times New Roman', 20))
        email_entry.place(relx=0.45, rely=0.45,x=-7, anchor='center', width=600)

        password_label = Label(user_register_window, text="Password:", bg="powderblue", font=('Times New Roman', 20))
        password_label.place(relx=0.2, rely=0.55,x=-10, anchor='center')
        password_entry = Entry(user_register_window, font=('Times New Roman', 20))
        password_entry.place(relx=0.35, rely=0.55,x=-5, anchor='center', width=300)

        # Login Button
        login_button = Button(user_register_window, text='Register', font=('Times New Roman', 20, 'bold'),command=lambda:cn.user_register(cn,first_name_entry.get(),last_name_entry.get(),email_entry.get(),password_entry.get()))
        login_button.place(relx=0.5, rely=0.7, anchor='center', width=250)

        # Register Button
        register_button = Button(user_register_window, text='Login / Register', font=('Times New Roman', 20, 'bold'), 
                                command=lambda: self.change_window(user_register_window,self.user_login_register))
        register_button.place(relx=0.5, rely=0.8, anchor='center', width=250)

        user_register_window.mainloop()

    
    def user_page(self):

        user_page_window = Tk()
        self.create_window(user_page_window,"User Page")

        title = Label(user_page_window, text="User Page", bg="powderblue", font=('Times New Roman',80,'bold'))
        title.place(anchor='center',relx='0.5',rely='0.25')

        request_book_button = Button(user_page_window, text='Request a Book',font=('Times New Roman',20,'bold'))
        request_book_button.place(relx=0.5,rely=0.5,x=-300,anchor='center',width=250)

        request_history_button = Button(user_page_window,text='Request History',font=('Times New Roman',20,'bold'))
        request_history_button.place(relx=0.5,rely=0.5,x=0,anchor='center',width=250)

        homepage_button = Button(user_page_window, text='Home Page',font=('Times New Roman',20,'bold'),command=lambda:self.change_window(user_page_window,self.homepage))
        homepage_button.place(relx=0.5,rely=0.5,x=300,anchor='center',width=250)
        
        user_page_window.mainloop()


    def add_book(self):
        add_book_window = Tk()
        self.create_window(add_book_window, "Add Book")

        title = Label(add_book_window, text="Add Book", bg="powderblue", font=('Times New Roman', 80, 'bold'))
        title.place(anchor='center', relx='0.5', rely='0.12')

        book_name_label = Label(add_book_window, text="Book Name:", bg="powderblue", font=('Times New Roman', 20))
        book_name_label.place(relx=0.2, rely=0.35, anchor='center')
        book_name_entry = Entry(add_book_window, font=('Times New Roman', 20))
        book_name_entry.place(relx=0.35, rely=0.35, anchor='center', width=300)

        author_name_label = Label(add_book_window, text="Author Name:", bg="powderblue", font=('Times New Roman', 20))
        author_name_label.place(relx=0.6, rely=0.35, anchor='center')
        author_name_entry = Entry(add_book_window, font=('Times New Roman', 20))
        author_name_entry.place(relx=0.75, rely=0.35, anchor='center', width=300)

        isbn_label = Label(add_book_window, text="ISBN:", bg="powderblue", font=('Times New Roman', 20))
        isbn_label.place(relx=0.2, rely=0.45, x=-30, anchor='center')
        isbn_entry = Entry(add_book_window, font=('Times New Roman', 20))
        isbn_entry.place(relx=0.45, rely=0.45, x=-7, anchor='center', width=600)

        # Fixing the issue here: Passing the entries' values correctly when the button is clicked.
        add_book_button = Button(add_book_window, text='Add Book', font=('Times New Roman', 20, 'bold'),
                                command=lambda: cn.add_book_to_db(cn,isbn_entry.get(), book_name_entry.get(), author_name_entry.get()))
        add_book_button.place(relx=0.5, rely=0.7, anchor='center', width=250)

        back_button = Button(add_book_window, text='Back', font=('Times New Roman', 20, 'bold'), 
                            command=lambda: self.change_window(add_book_window, self.admin_page))
        back_button.place(relx=0.5, rely=0.8, anchor='center', width=250)

        add_book_window.mainloop()


    def delete_book(self):
        display_issued_book_window = Tk()
        self.create_window(display_issued_book_window, "Delete Book")

        title = Label(display_issued_book_window, text="Delete Book", bg="powderblue", font=('Times New Roman', 80, 'bold'))
        title.place(anchor='center', relx='0.5', rely='0.12')

        book_id_label = Label(display_issued_book_window, text="Book Id:", bg="powderblue", font=('Times New Roman', 20))
        book_id_label.place(relx=0.25, rely=0.30, anchor='center')
        book_id_entry = Entry(display_issued_book_window, font=('Times New Roman', 20))
        book_id_entry.place(relx=0.40, rely=0.30, anchor='center', width=300)

        delete_book_button = Button(display_issued_book_window, text='Delete Book', font=('Times New Roman', 20, 'bold'),command=lambda:cn.delete_book(cn,book_id_entry.get(),display_issued_book_window))
        delete_book_button.place(relx=0.65, rely=0.30, anchor='center',width=250)

        book_data = cn.show_available_book(cn)
        style = ttk.Style()
        style.configure("Treeview.Heading", background="lightblue", foreground="black", font=("Arial", 12, "bold"))

        style.configure("Treeview", background="powderblue", fieldbackground="powderblue", foreground="black", font=("Arial", 10))
        columns = ("Book ID", "ISBN", "Book Name")

        tree = ttk.Treeview(display_issued_book_window, columns=columns, show="headings")
        tree.heading("Book ID", text="Book ID")
        tree.heading("ISBN", text="ISBN")
        tree.heading("Book Name", text="Book Name")

        # Define column widths
        tree.column("Book ID", width=100)
        tree.column("ISBN", width=150)
        tree.column("Book Name", width=250)


        for book in book_data:
            tree.insert('', END, values=book)

        tree.place(relx=0.5, rely=0.5, anchor='center')

        back_button = Button(display_issued_book_window, text='Back', font=('Times New Roman', 20, 'bold'), 
                            command=lambda: self.change_window(display_issued_book_window, self.admin_page))
        back_button.place(relx=0.5, rely=0.8, anchor='center', width=250)


        display_issued_book_window.mainloop()


    def issue_book(self):
        display_issued_book_window = Tk()
        self.create_window(display_issued_book_window, "Delete Book")

        title = Label(display_issued_book_window, text="Issue Book", bg="powderblue", font=('Times New Roman', 80, 'bold'))
        title.place(anchor='center', relx='0.5', rely='0.12')

        book_data = cn.request_book(cn)
        style = ttk.Style()

        style.configure("Treeview", background="powderblue", fieldbackground="powderblue", foreground="black", font=("Arial", 10))
        columns = ("User Id","Book Id","User Name", "Book Name")

        tree = ttk.Treeview(display_issued_book_window, columns=columns, show="headings")
        tree.heading("User Id", text="User Id")
        tree.heading("Book Id", text="Book Id")
        tree.heading("User Name", text="User Name")
        tree.heading("Book Name", text="Book Name")

        # Define column widths
        tree.column("User Id", width=100)
        tree.column("Book Id", width=100)
        tree.column("User Name", width=100)
        tree.column("Book Name", width=250)


        for book in book_data:
            tree.insert('', END, values=book)

        tree.place(relx=0.5, rely=0.5, anchor='center')

        issue_button = Button(display_issued_book_window, text='Issue', font=('Times New Roman', 20, 'bold'), 
                            command=lambda:cn.issue_book(cn,tree.item(tree.selection())['values']) )
        issue_button.place(relx=0.4, rely=0.8, anchor='center', width=250)

        back_button = Button(display_issued_book_window, text='Back', font=('Times New Roman', 20, 'bold'), 
                            command=lambda: self.change_window(display_issued_book_window, self.admin_page))
        back_button.place(relx=0.6, rely=0.8, anchor='center', width=250)

        display_issued_book_window.mainloop()


    def display_issued_book(self):
        display_issued_book_window = Tk()
        self.create_window(display_issued_book_window, "Issued Book")

        title = Label(display_issued_book_window, text="Issued Book", bg="powderblue", font=('Times New Roman', 80, 'bold'))
        title.place(anchor='center', relx='0.5', rely='0.12')

        book_data = cn.display_issued_book(cn)
        style = ttk.Style()

        style.configure("Treeview", background="powderblue", fieldbackground="powderblue", foreground="black", font=("Arial", 10))
        columns = ("User Id","Book Id","User Name", "Book Name")

        tree = ttk.Treeview(display_issued_book_window, columns=columns, show="headings")
        tree.heading("User Id", text="User Id")
        tree.heading("Book Id", text="Book Id")
        tree.heading("User Name", text="User Name")
        tree.heading("Book Name", text="Book Name")

        # Define column widths
        tree.column("User Id", width=100)
        tree.column("Book Id", width=100)
        tree.column("User Name", width=100)
        tree.column("Book Name", width=250)


        for book in book_data:
            tree.insert('', END, values=book)

        tree.place(relx=0.5, rely=0.5, anchor='center')

        back_button = Button(display_issued_book_window, text='Back', font=('Times New Roman', 20, 'bold'), 
                            command=lambda: self.change_window(display_issued_book_window, self.admin_page))
        back_button.place(relx=0.5, rely=0.8, anchor='center', width=250)

        display_issued_book_window.mainloop()


if __name__ == "__main__":
    obj = App()
    obj.homepage()

