import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, key):
        self.val = key
        self.children = []

def add_child(root, key):
    child = Node(key)
    root.children.append(child)
    return child

def preorder(root):
    result = []
    def traverse(node):
        result.append(str(node.val))
        for child in node.children:
            traverse(child)
    traverse(root)
    return ' -> '.join(result)

def postorder(root):
    result = []
    for child in root.children:
        result.append(postorder(child))
    result.append(str(root.val))
    return ' -> '.join(result)



class Interface:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.title("Company Organizational Structure")

        main_label = tk.Label(self.root, text="Company Organizational Structure", font=("Times New Roman", 45))
        main_label.grid(row=0, column=1, pady=20)

        button_width = 20  # Set a fixed width for all buttons
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
        preTrav = preorder(ceo)
        messagebox.showinfo("Pre-Order Traversal", preTrav)

    def in_order_messagebox(self):
        messagebox.showinfo("In-Order Traversal", "In-Order Traversal is currently unavailable in this Tree")

    def post_order_messagebox(self):
        postTrav = postorder(ceo)
        messagebox.showinfo("Post-Order Traversal", postTrav)

ceo = Node("Engr. Carlo")
mng1 = add_child(ceo, "Bob")
mng2 = add_child(ceo, "Eve")
mng3 = add_child(ceo, "Hannah")
add_child(mng1, "Beth")
add_child(mng1, "Allieson")
add_child(mng2, "Kennedick")
add_child(mng2, "Garcia")
add_child(mng3, "Ian")
add_child(mng3, "Franchesca")

preorder(ceo)
print()
postorder(ceo)

root = tk.Tk()
interface = Interface(root)
root.mainloop()

