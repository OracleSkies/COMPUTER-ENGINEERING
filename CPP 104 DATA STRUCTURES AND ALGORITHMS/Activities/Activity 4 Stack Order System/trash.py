def fullOrderWindow(self):

        self.fullOrderWindow = tk.Toplevel(self.root)
        self.fullOrderWindow.title("Empty Order")
        self.fullOrderWindow.geometry("400x300")
        self.fullOrderWindow.configure(bg='midnight blue')

        emptyLabel = tk.Label(self.fullOrderWindow, text="Empty Order", font=('Arial', 22), bg='midnight blue', fg='white')
        emptyLabel.pack(pady=10)

        display_emptyLabel = tk.Label(self.fullOrderWindow, text="You have no orders in your list", font=('Arial', 15), bg='midnight blue', fg='white')
        display_emptyLabel.pack(pady=10)

        confirm_buttonframe = tk.LabelFrame(self.fullOrderWindow, bg='midnight blue')
        confirm_buttonframe.pack(fill='x', padx=20, pady=20)
        confirm_buttonframe.columnconfigure(0, weight=1)

        confirm_back_button = tk.Button(confirm_buttonframe, text="Back", font=('Arial', 20), bg='royalblue3', fg='white', command=self.fullOrderWindow.destroy)
        confirm_back_button.grid(row=0, column=0, pady=10, sticky=tk.W+tk.E)