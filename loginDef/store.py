import tkinter as tk
from tkinter import messagebox
import connect


def go(customer_id):
    db = connect.get_connection()

    goods_cursor = db.cursor()
    query = "SELECT good_name, count, price, discount, good_id ,net_profit FROM goods"
    goods_cursor.execute(query)
    fetched_goods = goods_cursor.fetchall()

    goods_ui = {}
    cart = []

    def add_transaction(total_price, total_cash_back, net):
        cursor2 = db.cursor()
        query = "INSERT INTO trans (c_id, t_price, discount, t_net_profit) VALUES (%s, %s, %s,%s)"
        cursor2.execute(query, (customer_id, total_price, total_cash_back, net))


    def add_to_cart(item, count_var, btn):
        if count_var.get() <= 0:
            messagebox.showerror("Error", f"{item[0]} is out of stock!")
            btn.config(state=tk.DISABLED)
            return

        cart.append({
            "id": item[4],                 
            "name": item[0],               
            "price": item[2],
            "cach_back": item[3], 
            "net_profit": item[5]
        })

        cart_listbox.insert(
            tk.END,
            f"{item[0]} - price: {item[2]} EGP - cach_back: {item[3]} EGP"
        )

        goods_cursor.execute(
            "UPDATE goods SET count = count - 1 WHERE good_id = %s",
            (item[4],)
        )

        count_var.set(count_var.get() - 1)

        if count_var.get() == 0:
            btn.config(state=tk.DISABLED)

    def pay():
        if not cart:
            messagebox.showwarning("Warning", "Cart is empty!")
            return

        total_price = sum(item['price'] for item in cart)
        total_cash_back = sum(item['cach_back'] for item in cart)
        total_net_profit = sum(item['net_profit'] for item in cart)

        cursor1 = db.cursor()

        query_cachback = "select cash_back from customer where customer_id = %s"

        cursor1.execute(query_cachback, (customer_id,))
        result = cursor1.fetchone()

        if result[0] > 0 and result[0] >= total_price:
            remaining_price = 0
            query_pay = f"update customer set cash_back = cash_back - %s where customer_id = %s"
            cursor1.execute(query_pay, (total_price, customer_id))

        elif result[0] > 0 and result[0] < total_price:
            remaining_price = total_price - result[0]
            query_pay = f"update customer set cash_back = 0 where customer_id = %s"
            cursor1.execute(query_pay, (customer_id,))    

        else:
            remaining_price = total_price

        acount_cach_back = result[0] + total_cash_back - total_price + remaining_price

        messagebox.showinfo("Payment", f"""Total amount: {total_price} EGP
cash back: {total_cash_back} EGP
your acount cash back before payment: {result[0]} EGP
your remaining amount to pay: {remaining_price} EGP
your acount cash back after payment: {acount_cach_back} EGP
Payment successful!""")

        query_update_cashback = "update customer set cash_back = %s where customer_id = %s"
        cursor1.execute(query_update_cashback, (acount_cach_back, customer_id))

        add_transaction(total_price,total_cash_back,(total_net_profit-total_cash_back))

        cart.clear()
        cart_listbox.delete(0, tk.END)     
        db.commit()
        root.destroy()

    def remove_from_cart():
        selected = cart_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select item to remove")
            return

        index = selected[0]
        item = cart.pop(index)
        cart_listbox.delete(index)

        try:
            goods_cursor.execute(
                "UPDATE goods SET count = count + 1 WHERE good_id = %s",
                (item["id"],)
            )
            db.commit()

            ui = goods_ui[item["id"]]
            ui["count_var"].set(ui["count_var"].get() + 1)
            ui["button"].config(state=tk.NORMAL)
        except Exception as e:
            db.rollback()
            messagebox.showerror("DB Error", str(e))

    
    root = tk.Tk()
    root.title("Super Market")

    window_width = 1000
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    goods_container = tk.LabelFrame(root, text="Goods List", padx=5, pady=5)
    goods_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(goods_container)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(goods_container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    goods_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=goods_frame, anchor="nw")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    goods_frame.bind("<Configure>", on_frame_configure)

    for widget in goods_frame.winfo_children():
        widget.destroy()

    for item in fetched_goods:
        frame = tk.Frame(goods_frame)
        frame.pack(fill=tk.X, pady=5)

        count_var = tk.IntVar(value=item[1])

        label = tk.Label(
            frame,
            text=f"{item[0]} | price: {item[2]} | discount: {item[3]} | count:",
            width=50,
            anchor="w"
        )
        label.pack(side=tk.LEFT)

        count_label = tk.Label(frame, textvariable=count_var, width=5)
        count_label.pack(side=tk.LEFT)

        btn = tk.Button(frame, text="Add")
        btn.pack(side=tk.RIGHT)

        if item[1] == 0:
            btn.config(state=tk.DISABLED)

        btn.config(command=lambda i=item, cv=count_var, b=btn: add_to_cart(i, cv, b))

        goods_ui[item[4]] = {
            "count_var": count_var,
            "button": btn
        }

    cart_frame = tk.LabelFrame(root, text="Cart", padx=20, pady=10)
    cart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    cart_listbox = tk.Listbox(cart_frame, width=45)
    cart_listbox.pack(pady=10)

    remove_btn = tk.Button(
        cart_frame,
        text="Remove Selected",
        bg="red",
        fg="white",
        command=remove_from_cart
    )
    remove_btn.pack(pady=5)

    pay_btn = tk.Button(cart_frame, text="Pay", bg="green", fg="white", command=pay)
    pay_btn.pack(pady=10)

    root.mainloop() 
