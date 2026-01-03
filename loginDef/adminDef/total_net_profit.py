import tkinter as tk
import connect

def display_net_profit():
    def show_net_profit(net_profit):

        def center_window(win, width=300, height=180):
            screen_width = win.winfo_screenwidth()
            screen_height = win.winfo_screenheight()
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2
            win.geometry(f"{width}x{height}+{x}+{y}")

        win = tk.Toplevel()
        win.title("Net Profit")
        center_window(win)
        win.resizable(False, False)

        tk.Label(
            win,
            text="Net Profit",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        tk.Label(
            win,
            text=f"{net_profit}",
            font=("Arial", 20),
            fg="green"
        ).pack(pady=10)

        tk.Button(
            win,
            text="Close",
            width=15,
            command=win.destroy
        ).pack(pady=10)

    db = connect.get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT SUM(t_net_profit) FROM trans")
    result = cursor.fetchone()

    cursor.close()
    db.close()


    root = tk.Tk()
    root.withdraw()

    show_net_profit(result[0] if result[0] is not None else 0)
