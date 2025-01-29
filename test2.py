import tkinter as tk

# Initialize sales data
sales = {"Chicken": 0,"Fries-70": 0, "Fries-100": 0, "Smokies": 0, "Smoothies": 0}

# Function to update sales
def add_sale(item):
    sales[item] += 1
    update_display()

# Function to update the display
def update_display():
    display_text.set(
        f"Sales:\nChicken {sales['Chicken']} \nFries-70: {sales['Fries-70']}\nFries-100: {sales['Fries-100']}\n"
        f"Smokies: {sales['Smokies']}\nSmoothies: {sales['Smoothies']}"
    )

# Create the GUI window
window = tk.Tk()
window.title("Sales Monitor")

# Display sales totals
display_text = tk.StringVar()
update_display()
display_label = tk.Label(window, textvariable=display_text, font=("Arial", 14))
display_label.pack(pady=10)

# Buttons for each product
for item in sales:
    button = tk.Button(
        window, text=f"Add {item}", font=("Arial", 12),
        command=lambda item=item: add_sale(item)
    )
    button.pack(pady=5)

# Run the app
window.mainloop()
