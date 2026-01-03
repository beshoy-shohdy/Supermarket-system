import tkinter as tk
from tkinter import messagebox
import connect

def change_discount():
    def center_window(win, w=350, h=220):
        win.update_idletasks()
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry(f"{w}x{h}+{x}+{y}")
    
    def change_discount_ui():
        name = entry_name.get()
        discount = entry_discount.get()
    
        if not name or not discount:
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        db=connect.get_connection()
        cursor = db.cursor()
    
        query = "select * from goods where good_name=%s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
    
        if not result:
            messagebox.showerror("Error", "Good not found with this name")
            return
    
    
        query = "update goods set discount=%s where good_name=%s"
        cursor.execute(query, (discount, name))
    
        messagebox.showinfo(
            "Success",
            f"Discount updated!\n\n"
            f"Good: {name}\n"
            f"New Discount: {discount}"
        )
    
        entry_name.delete(0, tk.END)
        entry_discount.delete(0, tk.END)
    
        db.commit()
        cursor.close()
        db.close()
        root.destroy()
    
    
    root = tk.Tk()
    root.title("Change Discount")
    
    center_window(root)
    root.resizable(False, False)
    
    tk.Label(root, text="Change Discount", font=("Arial", 14, "bold")).pack(pady=10)
    
    frame = tk.Frame(root)
    frame.pack(pady=10)
    
    tk.Label(frame, text="Good Name").grid(row=0, column=0, sticky="w", pady=5)
    entry_name = tk.Entry(frame, width=25)
    entry_name.grid(row=0, column=1)
    
    tk.Label(frame, text="New Discount").grid(row=1, column=0, sticky="w", pady=5)
    entry_discount = tk.Entry(frame, width=25)
    entry_discount.grid(row=1, column=1)
    
    tk.Button(
        root,
        text="Change Discount",
        width=20,
        height=2,
        bg="#2196F3",
        fg="white",
        command=change_discount_ui
    ).pack(pady=15)
    
    root.mainloop()
    