import tkinter as tk
from tkinter import PhotoImage, messagebox

class Patient_Management_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.title("Patient Management System")

        # Load the background image for the main window
        self.image_path = "Main Window BG.png"
        self.background_image_main = PhotoImage(file=self.image_path)

        self.image_path_subWindow = "Sub Window BG.png"
        self.background_subWindow = PhotoImage(file=self.image_path_subWindow)

        # Set the background image for the main window
        self.background_label = tk.Label(root, image=self.background_image_main)
        self.background_label.place(relwidth=1, relheight=1)

        # Adjust the grid to allow proper positioning
        for i in range(12):
            self.root.columnconfigure(i, weight=1)
        for i in range(11):
            self.root.rowconfigure(i, weight=1)

        # Positioning the buttons and label
        column_position = 9

        main_label = tk.Label(self.root, text="Patient Management System", font=("Times New Roman", 25, "bold"), bg="white")
        main_label.grid(row=0, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_add_patient = tk.Button(self.root, text="Add Patient", font=("Times New Roman", 20, "bold"), width=15, command=self.open_add_patient_window)
        button_add_patient.grid(row=1, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_serve_patient = tk.Button(self.root, text="Serve Patient", font=("Times New Roman", 20, "bold"), width=15, command=self.open_serve_patient_window)
        button_serve_patient.grid(row=2, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_current_patient = tk.Button(self.root, text="Current Patient", font=("Times New Roman", 20, "bold"), width=15, command=self.open_current_patient_window)
        button_current_patient.grid(row=3, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_pending_patient = tk.Button(self.root, text="Pending Patient", font=("Times New Roman", 20, "bold"), width=15, command=self.open_check_pending_list_window)
        button_pending_patient.grid(row=4, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_check_patient_list_if_full = tk.Button(self.root, text="Check Patient List", font=("Times New Roman", 20, "bold"), width=15, command=self.open_if_pending_full_window)
        button_check_patient_list_if_full.grid(row=5, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_main_exit = tk.Button(self.root, text="Exit", font=("Times New Roman", 20, "bold"), width=15, command=self.root.destroy)
        button_main_exit.grid(row=6, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

    def set_background(self, window):
        background_label = tk.Label(window, image=self.background_subWindow)
        background_label.place(relwidth=1, relheight=1)

    def open_add_patient_window(self):
        self.add_patient_window = tk.Toplevel(self.root)
        self.add_patient_window.title("Add Patient")
        self.add_patient_window.geometry("750x570")

        self.set_background(self.add_patient_window)

        self.add_patient_label = tk.Label(self.add_patient_window, text="Add Patient", font=("Times New Roman", 40, "bold"))
        self.add_patient_label.pack(pady=20)

        self.add_patient_labelframe = tk.LabelFrame(self.add_patient_window, text="Insert Name: ", font=("Times New Roman", 20, "bold"))
        self.add_patient_labelframe.pack(fill='x', padx=20, pady=20)

        self.add_patient_labelframe.columnconfigure(0, weight=1)
        self.add_patient_labelframe.columnconfigure(1, weight=1)

        self.add_patient_input_text = tk.Entry(self.add_patient_labelframe, font=("Times New Roman", 35))
        self.add_patient_input_text.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        self.button_add_patient_confirm = tk.Button(self.add_patient_labelframe, text="Confirm", font=("Times New Roman", 25, "bold"), command=self.confirm_add_patient)
        self.button_add_patient_confirm.grid(row=1, column=0, padx=15, pady=5, sticky=tk.W+tk.E)

        self.add_patient_backButton = tk.Button(self.add_patient_labelframe, text="Back", font=("Times New Roman", 25, "bold"), command=self.add_patient_window.destroy)
        self.add_patient_backButton.grid(row=1, column=1, padx=15, pady=5, sticky=tk.W+tk.E)

    def confirm_add_patient(self):
        messagebox.showinfo("Confirmation", "Patient added successfully!")

    def open_serve_patient_window(self):
        self.serve_patient_window = tk.Toplevel(self.root)
        self.serve_patient_window.title("Serve Patient")
        self.serve_patient_window.geometry("750x570")

        self.set_background(self.serve_patient_window)

        self.serve_patient_label = tk.Label(self.serve_patient_window, text="Serve Patient", font=("Times New Roman", 45, "bold"))
        self.serve_patient_label.pack(pady=20)

        self.serve_patient_labelframe = tk.LabelFrame(self.serve_patient_window, text="Serving Patient", font=("Times New Roman", 15, "bold"))
        self.serve_patient_labelframe.pack(fill='x', padx=20, pady=20)

        self.serve_patient_labelframe.columnconfigure(0, weight=1)
        self.serve_patient_labelframe.columnconfigure(1, weight=1)

        self.serve_patient_input_text = tk.Label(self.serve_patient_labelframe, text="Output", font=("Times New Roman", 35))
        self.serve_patient_input_text.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        self.button_serve_patient_confirm = tk.Button(self.serve_patient_labelframe, text="Serve", font=("Times New Roman", 25, "bold"), command=self.confirm_serve_patient)
        self.button_serve_patient_confirm.grid(row=1, column=0, padx=15, pady=5, sticky=tk.W+tk.E)

        self.serve_backButton = tk.Button(self.serve_patient_labelframe, text="Back", font=("Times New Roman", 25, "bold"), command=self.serve_patient_window.destroy)
        self.serve_backButton.grid(row=1, column=1, padx=15, pady=5, sticky=tk.W+tk.E)

    def confirm_serve_patient(self):
        messagebox.showinfo("Confirmation", "Patient served successfully!")

    def open_current_patient_window(self):
        self.current_patient_window = tk.Toplevel(self.root)
        self.current_patient_window.title("Current Patient")
        self.current_patient_window.geometry("750x570")

        self.set_background(self.current_patient_window)

        self.current_patient_label = tk.Label(self.current_patient_window, text="Check Current Patient", font=("Times New Roman", 40, "bold"))
        self.current_patient_label.pack(pady=20)

        self.current_patient_labelframe = tk.LabelFrame(self.current_patient_window, text="Current Patient", font=("Times New Roman", 15, "bold"))
        self.current_patient_labelframe.pack(fill='x', padx=20, pady=20)

        self.current_patient_labelframe.columnconfigure(0, weight=1)
        self.current_patient_labelframe.columnconfigure(1, weight=1)

        self.current_patient_info_label = tk.Label(self.current_patient_labelframe, text="Patient Name: Trinity", font=("Times New Roman", 20))
        self.current_patient_info_label.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        self.current_patient_back_button = tk.Button(self.current_patient_window, text="Back", font=("Times New Roman", 25, "bold"), command=self.current_patient_window.destroy)
        self.current_patient_back_button.pack(pady=20)

    def open_check_pending_list_window(self):
        self.check_pending_list = tk.Toplevel(self.root)
        self.check_pending_list.title("Pending Patients")
        self.check_pending_list.geometry("750x570")

        self.set_background(self.check_pending_list)

        self.check_pending_label = tk.Label(self.check_pending_list, text="Check Pending Patients", font=("Times New Roman", 45, "bold"))
        self.check_pending_label.pack(pady=20)

        self.check_pending_labelframe = tk.LabelFrame(self.check_pending_list, text="Pending Patients", font=("Times New Roman", 15, "bold"))
        self.check_pending_labelframe.pack(fill='x', padx=20, pady=20)

        self.check_pending_labelframe.columnconfigure(0, weight=1)
        self.check_pending_labelframe.columnconfigure(1, weight=1)

        self.pending_patient_info_label = tk.Label(self.check_pending_labelframe, text="Patient Name: Trinity", font=("Times New Roman", 20))
        self.pending_patient_info_label.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        self.pending_patient_back_button = tk.Button(self.check_pending_list, text="Back", font=("Times New Roman", 25, "bold"), command=self.check_pending_list.destroy)
        self.pending_patient_back_button.pack(pady=20)

    def open_if_pending_full_window(self):
        self.pending_list_is_full = tk.Toplevel(self.root)
        self.pending_list_is_full.title("Patient List is Full/ Not Full")
        self.pending_list_is_full.geometry("750x570")

        self.set_background(self.pending_list_is_full)

        self.pending_is_full_label = tk.Label(self.pending_list_is_full, text="Patient is Full/ Not Full", font=("Times New Roman", 40, "bold"))
        self.pending_is_full_label.pack(pady=20)

        self.pending_is_full_labelframe = tk.LabelFrame(self.pending_list_is_full, text="Patient is Full/ Not Full", font=("Times New Roman", 15, "bold"))
        self.pending_is_full_labelframe.pack(fill='x', padx=20, pady=20)

        self.pending_is_full_labelframe.columnconfigure(0, weight=1)
        self.pending_is_full_labelframe.columnconfigure(1, weight=1)

        self.pending_patient_info_label = tk.Label(self.pending_is_full_labelframe, text="Patient Name: Trinity", font=("Times New Roman", 20))
        self.pending_patient_info_label.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        self.pending_patient_back_button = tk.Button(self.pending_list_is_full, text="Back", font=("Times New Roman", 25, "bold"), command=self.pending_list_is_full.destroy)
        self.pending_patient_back_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = Patient_Management_System(root)
    root.mainloop()
