import tkinter as tk
from tkinter import messagebox

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.title("Company Organizational Structure")

        main_label = tk.Label(self.root, text="Company Organizational Structure", font=("Times New Roman", 45))
        main_label.grid(row=0, column=1, pady=20)

        button_width = 20  # Set a fixed width for all buttons

        add_employee = tk.Button(self.root, text="Add Employee", font=("Times New Roman", 30), width=button_width, command=self.open_add_employee_window)
        add_employee.grid(row=1, column=1, pady=10)

        pre_order_button = tk.Button(self.root, text="Pre-Order Traversal", font=("Times New Roman", 30), width=button_width, command=self.pre_order_messagebox)
        pre_order_button.grid(row=2, column=1, pady=10)

        in_order_button = tk.Button(self.root, text="In-Order Traversal", font=("Times New Roman", 30), width=button_width, command=self.in_order_messagebox)
        in_order_button.grid(row=3, column=1, pady=10)

        post_order_button = tk.Button(self.root, text="Post-Order Traversal", font=("Times New Roman", 30), width=button_width, command=self.post_order_messagebox)
        post_order_button.grid(row=4, column=1, pady=10)

        exit_button = tk.Button(self.root, text="Exit", font=("Times New Roman", 30), width=button_width, command=self.root.destroy)
        exit_button.grid(row=5, column=1, pady=20)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

    def open_add_employee_window(self):
        self.add_employee_window = tk.Toplevel(self.root)
        self.add_employee_window.title("Add Employee Window")
        self.add_employee_window.geometry("750x570")

        self.add_superior_labelframe = tk.LabelFrame(self.add_employee_window, text="Superior", font=("Times New Roman", 20))
        self.add_superior_labelframe.pack(pady=20, padx=20, fill="x")

        self.add_superior_input = tk.Entry(self.add_superior_labelframe, font=("Times New Roman", 30))
        self.add_superior_input.pack(pady=10, padx=10, fill="x")

        self.add_employee_labelframe = tk.LabelFrame(self.add_employee_window, text="Employee", font=("Times New Roman", 20))
        self.add_employee_labelframe.pack(pady=20, padx=20, fill="x")

        self.add_employee_input = tk.Entry(self.add_employee_labelframe, font=("Times New Roman", 30))
        self.add_employee_input.pack(pady=10, padx=10, fill="x")

        confirm_button = tk.Button(self.add_employee_window, text="Confirm", font=("Times New Roman", 20))
        confirm_button.pack(pady=20, padx=20)

        back_button = tk.Button(self.add_employee_window, text="Back", font=("Times New Roman", 20), command=self.add_employee_window.destroy)
        back_button.pack(pady=20, padx=20)

    def pre_order_messagebox(self):
        messagebox.showinfo("Pre-Order Traversal", "This will perform a pre-order traversal.")

    def in_order_messagebox(self):
        messagebox.showinfo("In-Order Traversal", "This will perform an in-order traversal.")

    def post_order_messagebox(self):
        messagebox.showinfo("Post-Order Traversal", "This will perform a post-order traversal.")

root = tk.Tk()
interface = Interface(root)
root.mainloop()
