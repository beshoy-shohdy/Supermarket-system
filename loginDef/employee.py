import tkinter as tk
from employeeDef import add_customer,add_good, change_discount

def employee_panel(employee_name):
    root = tk.Tk()
    root.title("Employee Panel")

    window_width = 400
    window_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(False, False)

    title_label = tk.Label(
        root,
        text=f"Hi, {employee_name}",
        font=("Arial", 20, "bold")
    )
    title_label.pack(pady=20)

    btn_add_customer = tk.Button(
        root,
        text="Add Customer",
        width=20,
        height=2,
        command=lambda: add_customer.add_customer(root)
    )
    btn_add_customer.pack(pady=5)

    btn_change_discount = tk.Button(
        root,
        text="Change Discount",
        width=20,
        height=2,
        command=change_discount.change_discount
    )
    btn_change_discount.pack(pady=5)

    btn_add_goods = tk.Button(
        root,
        text="Add Goods",
        width=20,
        height=2,
        command=add_good.add_good
    )
    btn_add_goods.pack(pady=5)
    root.mainloop()     