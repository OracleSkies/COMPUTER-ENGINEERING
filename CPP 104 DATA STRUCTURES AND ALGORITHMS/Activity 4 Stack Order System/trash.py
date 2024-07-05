import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2 (spans 2 columns)")
label3 = tk.Label(root, text="Label 3 (spans 2 rows)")

# Place label1 in row 0, column 0, spanning 1 column and 1 row (default)
label1.grid(row=0, column=0)

# Place label2 in row 1, column 0, spanning 2 columns and 1 row
label2.grid(row=1, column=0, columnspan=2)

# Place label3 in row 0, column 1, spanning 1 column and 2 rows
label3.grid(row=0, column=1, rowspan=2)

root.mainloop()