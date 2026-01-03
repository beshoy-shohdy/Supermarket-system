import tkinter as tk
from tkinter import messagebox
import connect

def add_good():
    def center_window(window, width=400, height=350):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        window.geometry(f"{width}x{height}+{x}+{y}")

    def add_good_ui():
        try:
            name = entry_name.get()
            count = int(entry_count.get())
            price = float(entry_price.get())
            profit = float(entry_profit.get())
            discount = float(entry_discount.get() or 0)
        except ValueError:
            messagebox.showerror("Error", "check the entered data")
            return  

        db = connect.get_connection()
        cursor = db.cursor()

        query = "select * from goods where good_name=%s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()

        if result:
            query = "update goods set count=count+%s where good_name=%s"
            cursor.execute(query, (count, name))
        else:
            query = "insert into goods (good_name,count,price, net_profit, discount) values (%s, %s, %s, %s, %s)"
            cursor.execute(query, (name, count, price, profit, discount))

        messagebox.showinfo(
            "Success",
            f"Good Added:\n\n"
            f"Name: {name}\n"
            f"Count: {count}\n"
            f"Price: {price}\n"
            f"Net Profit: {profit}\n"
            f"Discount: {discount}"
        )

        entry_name.delete(0, tk.END)
        entry_count.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_profit.delete(0, tk.END)
        entry_discount.delete(0, tk.END)

        db.commit()
        cursor.close()
        db.close()
        root.destroy()



    root = tk.Tk()
    root.title("Add Good")

    center_window(root, 400, 350)
    root.resizable(False, False)

    tk.Label(root, text="Add New Good", font=("Arial", 16, "bold")).pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text="Name").grid(row=0, column=0, sticky="w", pady=5)
    entry_name = tk.Entry(frame, width=30)
    entry_name.grid(row=0, column=1)

    tk.Label(frame, text="Count").grid(row=1, column=0, sticky="w", pady=5)
    entry_count = tk.Entry(frame, width=30)
    entry_count.grid(row=1, column=1)

    tk.Label(frame, text="Price").grid(row=2, column=0, sticky="w", pady=5)
    entry_price = tk.Entry(frame, width=30)
    entry_price.grid(row=2, column=1)

    tk.Label(frame, text="Net Profit").grid(row=3, column=0, sticky="w", pady=5)
    entry_profit = tk.Entry(frame, width=30)
    entry_profit.grid(row=3, column=1)

    tk.Label(frame, text="Discount").grid(row=4, column=0, sticky="w", pady=5)
    entry_discount = tk.Entry(frame, width=30)
    entry_discount.grid(row=4, column=1)

    tk.Button(
        root,
        text="Add Good",
        width=20,
        height=2,
        bg="#4CAF50",
        fg="white",
        command=add_good_ui
    ).pack(pady=20)

    root.mainloop()