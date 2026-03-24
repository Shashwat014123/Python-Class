import tkinter as tk

root = tk.Tk()
root.title("Calories Calculator")

foods = {
    "Apple": 95,
    "Banana": 105,
    "Orange": 62,
    "Bread": 80,
    "Rice": 200,
    "Chicken": 165,
    "Fish": 120,
    "Egg": 78,
    "Milk": 150,
    "Cheese": 113,
}

selected_vars = {}

for i, food in enumerate(foods):
    var = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=food, variable=var)
    checkbox.grid(row=i, column=0, sticky="w")  # ✅ use ONLY grid
    selected_vars[food] = var

def calculate_total():
    total = 0
    for food in foods:
        if selected_vars[food].get() == 1:
            total += foods[food]
    result_label.config(text=f"Total Calories: {total}")

calc_button = tk.Button(root, text="Calculate Total Calories", command=calculate_total)
calc_button.grid(row=len(foods), column=0, pady=10)

result_label = tk.Label(root, text="Total Calories: 0")
result_label.grid(row=len(foods)+1, column=0)

root.mainloop()