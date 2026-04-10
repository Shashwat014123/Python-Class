import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg") #TkAgg(Tkinter Anti-Grain Geometry)

root=tk.Tk()
root.title("Energy Usage Calculator")

title = tk.Label(root, text="Appliance Energy Usage", font=("Helvetica", 16))
title.pack(pady=10)

appliance_wattage = {
    "TV": 100,                 # in watts
    "Fridge": 150,
    "Washing Machine": 500,
    "Computer": 200,
    "Fan": 75,
    "AC": 1500,
    "Food Processor": 300, 
    "Microwave": 1200, 
    "WiFi": 20
}

cost_per_kwh = 0.13  

#input frame for selecting appliances and hours of usage
input_frame = tk.LabelFrame(root, text="📋Appliance Selection & Usage (hrs/day)", font=("Arial", 12, "bold"), bg="#d95848")
input_frame.place(x=30, y=60, width=450, height=450)

#list of applicances
appliances = ["TV", "Fridge", "Washing Machine", "Computer", "Fan", "AC","WiFi", "Microwave", "Food Processor"]

selected_vars = {}
hours_entries = {}

#creating checkbuttons and entry for each appliance
for i, appliance in enumerate(appliances):
    var = tk.IntVar()
    chk = tk.Checkbutton(input_frame, text=appliance, variable=var)
    chk.grid(row=i, column=0, sticky='w',pady=10)

    hours_label = tk.Label(input_frame, text="Hours:")
    hours_label.grid(row=i, column=1, padx=5)

    entry = tk.Entry(input_frame, width=5)
    entry.grid(row=i, column=2)

    selected_vars[appliance] = var
    hours_entries[appliance] = entry

def calculate():
    output_text.delete("1.0", tk.END)  # Clear previous output
    output_text.insert(tk.END, "Appliance-wise Energy Usage:\n\n")
 
    total_energy = 0  # Initialize total energy variable
    total_cost = 0  # Initialize total cost variable
 
    for appliance in appliances:
        if selected_vars[appliance].get() == 1:  # If checkbox is selected
            try:
                hours = float(hours_entries[appliance].get())  # Get entered hours
                energy_kwh = round((appliance_wattage[appliance] * hours) / 1000, 2) # Convert to kWh
                cost = round(energy_kwh * cost_per_kwh, 2)  # Calculate cost
                total_energy += energy_kwh
                total_cost+=cost
                output_text.insert(tk.END, f"{appliance}: {hours} hrs × {appliance_wattage[appliance]}W = {energy_kwh:.2f} kWh/day\n")
            except ValueError:
                output_text.insert(tk.END, f"{appliance}: Invalid hours input!\n")
 
    output_text.insert(tk.END, f"\nTotal Energy Used Per Day: {total_energy:.2f} kWh")
    output_text.insert(tk.END, f"\nTotal Cost Per Day: ${total_cost:.2f}")

    #--Calculate Button--#
btn = tk.Button(root, text="Calculate", command=lambda: calculate(), bg="#d95848", fg="white", font=("Arial", 12, "bold"))
btn.place(x=550, y=60)

#---Class 15: Scrollable Text Summary Output---#
summary_frame = tk.LabelFrame(root)
summary_frame.pack(padx=10, pady=10, fill='both', expand=True)

scrollbar = tk.Scrollbar(summary_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(summary_frame, height=10, yscrollcommand=scrollbar.set, wrap='word')
output_text.pack(fill='both', expand=True)

scrollbar.config(command=output_text.yview)

#--Lesson 16--#
#---Treview Table to show results---#
table_frame = tk.LabelFrame(root, text="Applicance-wise Energy & Cost", padx=10, pady=5, font=("Arial", 12, "bold"), bg="#d95848")
table_frame.place(x=500, y=110, width=460, height=250)

tree=ttk.Treeview(table_frame, columns=("Appliance", "Hours", "kWh", "Cost"), show="headings")
    
tree.heading("Appliance", text="Appliance")
tree.heading("Hours", text="Hours")
tree.heading("kWh", text="Energy (kWh)")
tree.heading("Cost", text="Cost (USD)")

tree.column("Appliance", width=150)
tree.column("Hours", width=100)
tree.column("kWh", width=150)
tree.column("Cost", width=150)

tree.place(fill='both', expand=True)

#scrollbar for the treeview
tree_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=tree_scrollbar.set)
tree_scrollbar.place(x=445, y=0, height=220)

#summary frame
results_frame = tk.LabelFrame(root, text="Summary & Suggestions",  font=("Arial", 12, "bold"), bg="#d95848")
results_frame.place(x=30, y=530, width=930, height=230)

#--Output box with Scrollbar--#
output_frame=tk.Frame(root)
output_frame.place(x=20, y=510, width=760, height=70)

scrollbar=tk.Scrollbar(output_frame)
scrollbar.place(side=tk.RIGHT, fill=tk.Y)

result_text=tk.Text(output_frame, height=4, yscrollcommand=scrollbar.set, wrap='word')
result_text.place(fill='both', expand=True)

scrollbar.config(command=result_text.yview)

#Calculation logic
def calculate():
    tree.delete(*tree.get_children()) #delete previous treeview entries
    result_text.delete("1.0", tk.END) #clear previous summary output

    selected_appliances = [appliance for appliance in appliances if selected_vars[appliance].get() == 1] 
    #special line 
    #looks through list of appliacnes and checks if each checkbox is selected
    #checks which appliances are selected 
    #creates a new list of those appliances to be used in calculations


    if not selected_appliances: #if there is nothing in the list of selected appliances
        messagebox.showwarning("No Appliances Selected", "Please select at least one appliance.") #show warning message if no appliances are selected
        return
    
    try:
        usage_hours = {appliance: float(hours_entries[appliance].get()) for appliance in selected_appliances} #dictionary to loop through selected appliances and get the amount of hours used for each appliance. Then converting it to a float for calculations
        energy_consumed = {appliance: round((appliance_wattage[appliance] * usage_hours[appliance]) / 1000, 2) for appliance in selected_appliances} #dictionary to store energy consumed for each selected appliance using a formula to convert watt-hours to kilowatt-hours
        costs = {appliance: round(energy_consumed[appliance] * cost_per_kwh, 2) for appliance in selected_appliances} #dictionary to loop across the selected appiances and store cost for each of them. Then multiplying energy consumed by cost per kWh
        
        daily = round(sum(energy_consumed.values()), 2) #taking dictionary values from engery_comsumed and adds them up to 2 decimal places to get the total energy consumed per day. Then rounding it to 2 decimal places
        monthly = round(daily * 30, 2) #daliy energy multiplied by 30 to get monthly energy up to 2 decimal places
        yearly = round(daily * 365, 2) #daily energy multiplied by 365 to get yearly energy up to 2 decimal places

        suggested_panels = round(daily/1.5) #calculating the number of solar panels needed to cover the daily energy usage
        solar_energy = round(suggested_panels * 1.5, 2) #total solar engery generated by the suggested number of panels

        saved_kWh = min(daily, solar_energy) #amount of energy saved by using solar panels
        saved_money = round(saved_kWh * cost_per_kwh, 2) #amount of money saved by using solar panels, calculated by multiplying saved energy by cost per kWh

        panel_cost = 250 #cost of one solar panel
        install_cost = 500 #cost of installing one solar panel
        total_cost = panel_cost * suggested_panels + install_cost #total cost of the solar power setup
        break_even = round(total_cost / saved_money, 1) if saved_money > 0 else "-" #

        for appliance in selected_appliances:
            tree.insert("", "end", values=(appliance, usage_hours[appliance], energy_consumed[appliance], f"${costs[appliance]:.2f}"))

            result_text = f"""
        📌 Daily Energy Usage: {daily} kWh
        🔋 Solar Energy Generated (Suggested Panels = {suggested_panels}): {solar_energy} kWh
        ____________________________________________________________________________________
 
        ✅ Savings if Solar is Used:
        - Daily Savings: {saved_kWh} kWh | ${saved_money}
        - Monthly Savings: {round(saved_kWh * 30, 2)} kWh | ${round(saved_money * 30, 2)}
        - Yearly Savings: {round(saved_kWh * 365, 2)} kWh | ${round(saved_money * 365, 2)}
        ____________________________________________________________________________________
        💰 Break-even Time: {break_even} days
        💸 Total Solar Setup Cost: ${total_cost}
        """
        result_text.insert(tk.END, result_text)
 
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all usage fields.") #show error message if there is an invalid input



root.mainloop()

#break-even point = when investments are equal to savings