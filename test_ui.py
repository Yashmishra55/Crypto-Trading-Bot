import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Test Entry")

style = ttk.Style()
style.theme_use('clam')
style.configure("TEntry", fieldbackground="#333333", foreground="white")

entry = ttk.Entry(root)
entry.pack(padx=20, pady=20)

root.mainloop()
