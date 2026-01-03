import tkinter as tk
from tkinter import messagebox
import connect

def add_customer(parent):

    def center_window(win, width=400, height=250):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        win.geometry(f"{width}x{height}+{x}+{y}")

    def add_customer_ui():
        name = name_var.get().strip()
        phone = phone_var.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "All fields are required")
            return

        if not phone.isdigit():
            messagebox.showerror("Error", "Phone must contain only numbers")
            return

        if len(phone) < 10:
            messagebox.showerror("Error", "Invalid phone number")
            return

        db = connect.get_connection()
        cursor = db.cursor()

        cursor.execute(
            "SELECT 1 FROM customer WHERE user_name=%s",
            (name,)
        )
        user_check = cursor.fetchone()

        cursor.execute(
            "SELECT 1 FROM customer WHERE phone=%s",
            (phone,)
        )
        phone_check = cursor.fetchone()

        if user_check or phone_check:
            messagebox.showerror(
                "Error",
                "User name or phone already exists"
            )
            cursor.close()
            db.close()
            return

        cursor.execute(
            "INSERT INTO customer (user_name, cash_back, phone) VALUES (%s, %s, %s)",
            (name, 0, phone)
        )
        db.commit()

        customer_id = cursor.lastrowid

        messagebox.showinfo(
            "Success",
            f"Customer Added Successfully\n\n"
            f"Name: {name}\n"
            f"Phone: {phone}\n"
            f"Customer ID: {customer_id}"
        )

        name_var.set("")
        phone_var.set("")

        cursor.close()
        db.close()
        parent.destroy()

    
    win = tk.Toplevel(parent)
    win.title("Add Customer")
    center_window(win)
    win.resizable(False, False)

    name_var = tk.StringVar()
    phone_var = tk.StringVar()

    tk.Label(
        win,
        text="Add Customer",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    form = tk.Frame(win)
    form.pack(pady=10)

    tk.Label(form, text="User name:", anchor="w").grid(row=0, column=0, pady=5)
    tk.Entry(form, textvariable=name_var, width=25).grid(row=0, column=1)

    tk.Label(form, text="Phone number:", anchor="w").grid(row=1, column=0, pady=5)
    tk.Entry(form, textvariable=phone_var, width=25).grid(row=1, column=1)

    tk.Button(
        win,
        text="Add Customer",
        width=20,
        command=add_customer_ui
    ).pack(pady=15)
