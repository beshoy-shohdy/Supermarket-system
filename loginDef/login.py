import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sys
import os

sys.path.append(os.path.dirname(__file__))
from . import connect
from . import store
from . import employee


db = connect.get_connection()

def login():
    username = username_var.get()
    password = password_var.get()
    is_employee = employee_type_var.get()
    
    if not username or not password:
        showinfo(title='Input Error', message='Please enter both username and password.')
        return

    if username == "admin" and password == "admin123" and is_employee == 1:
        showinfo(title='Login Status', message='Login successful! Welcome, admin.')
        root.destroy()
        import admin
        admin.admin_panel()
        return

    user_type = "employee" 
    if is_employee == 0:
        user_type = "customer"

    if user_type.lower() == "employee":
        query_name = "SELECT user_name FROM employee"
    else:
        query_name = "SELECT user_name FROM customer"

    name_check_cursor = db.cursor()
    name_check_cursor.execute(query_name)
    name_result = name_check_cursor.fetchall()

    user_check = 0
    for name in name_result:
        if name[0] == username:
            user_check = 1

    cont_check = 0
    if user_check == 1:
        if user_type.lower() == "employee":
            query_id = f"SELECT employee_id FROM employee WHERE user_name='{username}'"
        else:
            query_id = f"SELECT customer_id FROM customer WHERE user_name='{username}'"

        id_check_cursor = db.cursor()
        id_check_cursor.execute(query_id)
        pass_check = id_check_cursor.fetchone()

        if pass_check and pass_check[0] == int(password):
            cont_check = 1
            message = f"Login successful! Welcome, {username} ({user_type})."
        else:
            message = "Login failed. Please check your credentials."
        id_check_cursor.close()
    else:
        message = "Login failed. Please check your credentials."

    showinfo(title='Login Status', message=message)

    name_check_cursor.close()

    if cont_check == 1 and user_type.lower() == "customer":
        root.destroy()
        db.close()
        store.go(pass_check[0])
    elif cont_check == 1 and user_type.lower() == "employee":
        root.destroy()
        db.close()
        employee.employee_panel(username)


root = tk.Tk()
root.title("Login System")
style = ttk.Style(root)
style.theme_use('clam') 
root.resizable(False, False)


window_width = 350
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


username_var = tk.StringVar()
password_var = tk.StringVar()
employee_type_var = tk.IntVar(value=0)


main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.pack(fill='both', expand=True)

ttk.Label(main_frame, text="User name:").grid(column=0, row=0, sticky=tk.W, pady=5, padx=5)
username_entry = ttk.Entry(main_frame, width=30, textvariable=username_var)
username_entry.grid(column=1, row=0, sticky=tk.W, pady=5, padx=5)
username_entry.focus()

ttk.Label(main_frame, text="ID:").grid(column=0, row=1, sticky=tk.W, pady=5, padx=5)
password_entry = ttk.Entry(main_frame, width=30, textvariable=password_var, show="*")
password_entry.grid(column=1, row=1, sticky=tk.W, pady=5, padx=5)

employee_checkbox = ttk.Checkbutton(
    main_frame,
    text='Check if Employee',
    variable=employee_type_var,
    onvalue=1,
    offvalue=0
)
employee_checkbox.grid(column=1, row=2, sticky=tk.W, pady=10)

login_button = ttk.Button(
    main_frame,
    text='Login',
    command=login
)
login_button.grid(column=1, row=3, sticky=tk.E, pady=10)
