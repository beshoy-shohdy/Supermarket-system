import tkinter as tk
from adminDef import add_empolyee , total_net_profit

def admin_panel():
    root = tk.Tk()
    root.title("Admin Panel")

    window_width = 400
    window_height = 200

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(False, False)

    title_label = tk.Label(
        root,
        text=f"Hi, admin",
        font=("Arial", 20, "bold")
    )
    title_label.pack(pady=20)

    btn_add_customer = tk.Button(
        root,
        text="Add Employee",
        width=20,
        height=2,
        command=lambda: add_empolyee.add_employee(root)
    )
    btn_add_customer.pack(pady=5)

    btn_change_discount = tk.Button(
        root,
        text="total net profit",
        width=20,
        height=2,
        command=lambda: total_net_profit.display_net_profit()
    )
    btn_change_discount.pack(pady=5)
    root.mainloop()   