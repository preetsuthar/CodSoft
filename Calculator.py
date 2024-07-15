import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            messagebox.showerror("Error", "Invalid operator. Please select +, -, *, or /.")
            return
        
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

root = tk.Tk()
root.title("Simple Calculator")

num1_var = tk.StringVar()
num2_var = tk.StringVar()
operator_var = tk.StringVar(value="+")
result_var = tk.StringVar()

tk.Label(root, text="Enter the first number:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root, textvariable=num1_var)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter an operator (+, -, *, /):").grid(row=1, column=0, padx=10, pady=10)
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_menu.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the second number:").grid(row=2, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root, textvariable=num2_var)
entry_num2.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Result:").grid(row=4, column=0, padx=10, pady=10)
result_entry = tk.Entry(root, textvariable=result_var, state='readonly')
result_entry.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
