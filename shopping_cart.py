import tkinter as tk
from tkinter import ttk
items = {"book": 10, "snacks": 5, "toy": 20, "pencil": 2, "notebook": 8, "backpack": 30, "lunchbox": 15, "water bottle": 12, "headphones": 25, "smartphone": 200, "laptop": 500, "tablet": 300, "printer": 100, "monitor": 250, "keyboard": 50, "mouse": 30}

root = tk.Tk()

root.title("Shopping Cart")
root.geometry("400x300")
cart = []

for i, item in enumerate(items):
    selected_item= tk.IntVar()

    chk = tk.Checkbutton(root, text=f"{item} - ${items[item]}", variable=selected_item)
    chk.grid(row=i, column=0, sticky="w")
    cart.append((selected_item, item))

table_frame = tk.LabelFrame(root, text="Cart")
table_frame.place(x=200, y=20)

tree = ttk.Treeview(table_frame, columns=("Item", "Price"), show="headings")
tree.heading("Item", text="Item")
tree.heading("Price", text="Price")

tree.pack(fill="both", expand=True)

def add_to_cart():
    for selected_item, item in cart:
        if selected_item.get() == 1:
            tree.insert("", "end", values=(item, items[item]))

add_btn = tk.Button(root, text="Add to Cart", command=add_to_cart)
add_btn.place(x=20, y=450)

def calculate_total():
    total = 0
    for selected_item, item in cart:
        if selected_item.get() == 1:
            total += items[item]
    total_label.config(text=f"Total: ${total}")

total_label = tk.Label(root, text="Total: $0")
total_label.place(x=20, y=490)

total_btn = tk.Button(root, text="Calculate Total", command=calculate_total)
total_btn.place(x=20, y=520)

reset_btn = tk.Button(root, text="Reset Cart", command=lambda: [tree.delete(*tree.get_children()), total_label.config(text="Total: $0"), [selected_item.set(0) for selected_item, _ in cart]])
reset_btn.place(x=150, y=520)


root.mainloop()