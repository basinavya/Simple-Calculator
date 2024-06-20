import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Input Field
        input_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP)
        
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, bd=10, insertwidth=4, width=14, justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack()

        # Buttons Frame
        buttons_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE)
        buttons_frame.pack()

        # Buttons Layout
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', '^',
            '0', '.', '=', '+'
        ]

        row_val = 0
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(buttons_frame, text=button, font=('arial', 18, 'bold'), bd=8, padx=10, pady=10, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def click_event(self, key):
        if key == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero is undefined")
                self.input_text.set("")
                self.expression = ""
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.input_text.set("")
                self.expression = ""
        elif key == 'C':
            self.input_text.set("")
            self.expression = ""
        elif key == '√':
            try:
                result = str(math.sqrt(eval(self.expression)))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.input_text.set("")
                self.expression = ""
        elif key == '^':
            self.expression += '**'
            self.input_text.set(self.expression)
        else:
            self.expression += str(key)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
