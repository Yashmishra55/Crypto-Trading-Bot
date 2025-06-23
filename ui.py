import tkinter as tk
from tkinter import ttk, messagebox
from bot import BasicBot

bot = BasicBot()

# --- Order Placement ---
def place_order():
    symbol = symbol_entry.get().upper()
    side = side_var.get()
    order_type = type_var.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    if not symbol or not side or not order_type or not quantity:
        messagebox.showerror("Input Error", "Please fill in all required fields.")
        return

    try:
        quantity = float(quantity)
        price = float(price) if order_type == "LIMIT" else None
        result = bot.place_order(symbol, side, order_type, quantity, price)
        output_label.config(text=f"✅ Order Placed:\n{result}")
    except Exception as e:
        messagebox.showerror("Order Failed", str(e))

# --- Cancel All Orders ---
def cancel_all():
    try:
        symbol = symbol_entry.get().upper()
        if not symbol:
            messagebox.showerror("Symbol Missing", "Please enter a trading pair to cancel orders.")
            return
        result = bot.client.futures_cancel_all_open_orders(symbol=symbol)
        output_label.config(text=f"🧹 All open orders canceled:\n{result}")
    except Exception as e:
        messagebox.showerror("Cancel Failed", str(e))

# --- Show Balance ---
def show_balance():
    try:
        balance = bot.client.futures_account_balance()
        usdt_balance = next((item for item in balance if item['asset'] == 'USDT'), None)
        balance_label.config(text=f"💰 Balance (USDT): {usdt_balance['balance']}")
    except Exception as e:
        messagebox.showerror("Balance Error", str(e))

# --- UI Setup ---
root = tk.Tk()
root.title("💹 Binance Futures Testnet Trading Bot")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use('clam')

# Style setup for dark theme
style.configure("TLabel", background="#1e1e1e", foreground="white")
style.configure("TButton", padding=6, relief="flat", background="#333333", foreground="white")
style.configure("TCombobox", fieldbackground="#333333", background="#333333", foreground="white")

# Balance display
balance_label = ttk.Label(root, text="💰 Balance: Loading...")
balance_label.grid(row=0, column=0, columnspan=2, pady=10)
show_balance()

# --- Input Fields ---
tk.Label(root, text="Symbol (e.g., BTCUSDT):", bg="#1e1e1e", fg="white").grid(row=1, column=0, sticky="w")
symbol_entry = tk.Entry(root, bg="#333333", fg="white", insertbackground="white")
symbol_entry.grid(row=1, column=1)

tk.Label(root, text="Side:", bg="#1e1e1e", fg="white").grid(row=2, column=0, sticky="w")
side_var = tk.StringVar(value="BUY")
side_menu = ttk.Combobox(root, textvariable=side_var, values=["BUY", "SELL"])
side_menu.grid(row=2, column=1)

tk.Label(root, text="Order Type:", bg="#1e1e1e", fg="white").grid(row=3, column=0, sticky="w")
type_var = tk.StringVar(value="MARKET")
type_menu = ttk.Combobox(root, textvariable=type_var, values=["MARKET", "LIMIT"])
type_menu.grid(row=3, column=1)

tk.Label(root, text="Quantity:", bg="#1e1e1e", fg="white").grid(row=4, column=0, sticky="w")
quantity_entry = tk.Entry(root, bg="#333333", fg="white", insertbackground="white")
quantity_entry.grid(row=4, column=1)

tk.Label(root, text="Price (for LIMIT):", bg="#1e1e1e", fg="white").grid(row=5, column=0, sticky="w")
price_entry = tk.Entry(root, bg="#333333", fg="white", insertbackground="white")
price_entry.grid(row=5, column=1)

# Buttons
ttk.Button(root, text="📤 Place Order", command=place_order).grid(row=6, column=0, columnspan=2, pady=10)
ttk.Button(root, text="❌ Cancel All Orders", command=cancel_all).grid(row=7, column=0, columnspan=2)
ttk.Button(root, text="🔁 Refresh Balance", command=show_balance).grid(row=8, column=0, columnspan=2, pady=(5, 15))

# Output
output_label = ttk.Label(root, text="", wraplength=400, justify="left")
output_label.grid(row=9, column=0, columnspan=2)

root.mainloop()
