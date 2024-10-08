import tkinter as tk
from tkinter import messagebox, PhotoImage

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self): #checks if the Linked list is empty
        return self.head is None

    def append(self, data): #insert at end
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node_at_position(self, position): #deletes a node at a certain index or position
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for _ in range(position - 1):
            temp = temp.next
            if temp is None:
                return
        if temp is None or temp.next is None:
            return
        next_node = temp.next.next
        temp.next = None
        temp.next = next_node
    
    def delete_node(self, key): #Deletes node of a specific key
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
    
    def search(self, key): #Searches node with a specific key. Returns true if the key exists
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def displayName(self, key): #returns the key if it exist
        current = self.head
        while current:
            if current.data == key:
                return current.data
            current = current.next
        else:
            return "Patient does not exist"
    
    def length(self): #returns the current lenght of the list
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def listHead(self): #returns the head of the linked list
        if self.head:
            return self.head.data
        else:
            errorText = "There are no patients to serve yet"
            return errorText
        
    def isFull(self): #checks if the list is at max capacity (max at 10)
        return self.length() >= 10

    def displayPatients(self): #returns all the data inside the linked list
        current = self.head
        nodes = []
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes 

class Patient_Management_System:
    def __init__(self, root):
        self.link = LinkedList()
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

        # Positioning the buttons and label towards the right side of the window
        column_position = 9  # Move the buttons more to the right

        main_label = tk.Label(self.root, text="Patient Management System", font=("Times New Roman", 25, "bold"), bg="white")
        main_label.grid(row=0, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_add_patient = tk.Button(self.root, text="Add Patient", font=("Times New Roman", 20, "bold"), width=15, command=self.open_add_patient_window)
        button_add_patient.grid(row=1, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_serve_patient = tk.Button(self.root, text="Serve Patient", font=("Times New Roman", 20, "bold"), width=15, command=self.open_serve_patient_window)
        button_serve_patient.grid(row=2, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_current_patient = tk.Button(self.root, text="Current Patient", font=("Times New Roman", 20, "bold"), width=15, command=self.open_current_patient_window)
        button_current_patient.grid(row=3, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_pending_patient = tk.Button(self.root, text="Pending Patient List", font=("Times New Roman", 20, "bold"), width=15, command=self.open_check_pending_list_window)
        button_pending_patient.grid(row=4, column=column_position, columnspan=2, sticky=tk.W+tk.E, pady=10)

        button_check_patient_list_if_full = tk.Button(self.root, text="Patient Capacity", font=("Times New Roman", 20, "bold"), width=15, command=self.open_if_pending_full_window)
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

        self.button_add_patient_confirm = tk.Button(self.add_patient_labelframe, text="Confirm", font=("Times New Roman", 25, "bold"), command= lambda: self.confirm_add_patient(self.add_patient_input_text.get()))
        self.button_add_patient_confirm.grid(row=1, column=0, padx=15, pady=5, sticky=tk.W+tk.E)

        self.add_patient_backButton = tk.Button(self.add_patient_labelframe, text="Back", font=("Times New Roman", 25, "bold"), command=self.add_patient_window.destroy)
        self.add_patient_backButton.grid(row=1, column=1, padx=15, pady=5, sticky=tk.W+tk.E)

    def confirm_add_patient(self,patient):
        if self.link.isFull():
            messagebox.showinfo("Confirmation", "Patient capacity is full!")
            self.add_patient_window.destroy()
            return
        self.link.append(patient)
        messagebox.showinfo("Confirmation", f"{patient} added successfully!")
        self.add_patient_window.destroy()

    def open_serve_patient_window(self):
        self.serve_patient_window = tk.Toplevel(self.root)
        self.serve_patient_window.title("Serve Patient")
        self.serve_patient_window.geometry("750x570")

        self.set_background(self.serve_patient_window)

        self.serve_patient_label = tk.Label(self.serve_patient_window, text="Serve Patient", font=("Times New Roman", 45, "bold"))
        self.serve_patient_label.pack(pady=20)

        self.serve_patient_labelframe = tk.LabelFrame(self.serve_patient_window, text="Serving Patient", font=("Times New Roman", 15, "bold"))
        self.serve_patient_labelframe.pack(fill = 'x', padx=20, pady=20)

        self.serve_patient_labelframe.columnconfigure(0, weight=1)
        self.serve_patient_labelframe.columnconfigure(1, weight=1)

        self.serve_patient_input_text = tk.Label(self.serve_patient_labelframe, text= f"{self.link.listHead()}", font=("Times New Roman", 20))
        self.serve_patient_input_text.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        self.button_serve_patient_confirm = tk.Button(self.serve_patient_labelframe, text="Serve", font=("Times New Roman", 25, "bold"), command=self.confirm_serve_patient)
        self.button_serve_patient_confirm.grid(row=1, column=0, padx=15, pady=5, sticky=tk.W+tk.E)

        self.serve_backButton = tk.Button(self.serve_patient_labelframe, text="Back", font=("Times New Roman", 25, "bold"), command=self.serve_patient_window.destroy)
        self.serve_backButton.grid(row=1, column=1, padx=15, pady=5, sticky=tk.W+tk.E)

        #================== SECOND LABEL FRAME ========================

        self.search_serve_patient_labelframe = tk.LabelFrame(self.serve_patient_window, text="Search Patient", font=("Times New Roman", 15, "bold"))
        self.search_serve_patient_labelframe.pack(padx=0, pady=0)

        self.searchServePatientEntry = tk.Entry(self.search_serve_patient_labelframe, font = ("Times New Roman", 35))
        self.searchServePatientEntry.grid(row = 0, column = 0, padx = 15, pady = 5,sticky=tk.W+tk.E )

        self.button_serve_search_patient_confirm = tk.Button(self.search_serve_patient_labelframe, text="Serve", font=("Times New Roman", 25, "bold"), command = lambda: self.confirmSearchServePatient(self.searchServePatientEntry.get())) 
        self.button_serve_search_patient_confirm.grid(row=0, column=1, padx=15, pady=5, sticky=tk.W+tk.E)

        self.search_serve_patient_labelframe.columnconfigure(0, weight=1)
        self.search_serve_patient_labelframe.columnconfigure(1, weight=1)

    def confirmSearchServePatient(self,name):
        if self.link.search(name):
            self.link.delete_node(name)
            messagebox.showinfo("Confirmation", f"{name} was served successfully!")
            self.serve_patient_input_text.config(text= f"{self.link.listHead()}")
            self.serve_patient_window.destroy()
        else:
            messagebox.showinfo("Patient Name Error", f"There is no patient named {name} in the facility")
            
    def confirm_serve_patient(self):
        if self.link.head:
            messagebox.showinfo("Confirmation", f"{self.link.listHead()} was served successfully!")
            self.link.delete_node_at_position(0)
            self.serve_patient_window.destroy()
        else:
            messagebox.showinfo("Confirmation", "There are no patients to serve yet")
            self.serve_patient_window.destroy()
        
    def open_current_patient_window(self):
        self.current_patient_window = tk.Toplevel(self.root)
        self.current_patient_window.title("Current Patient")
        self.current_patient_window.geometry("750x350")

        self.set_background(self.current_patient_window)

        self.current_patient_label = tk.Label(self.current_patient_window, text="Current Patient", font=("Times New Roman", 40, "bold"))
        self.current_patient_label.pack(pady=20)

        self.current_patient_labelframe = tk.LabelFrame(self.current_patient_window, text="Current Patient", font=("Times New Roman", 15, "bold"))
        self.current_patient_labelframe.pack(fill='x', padx=20, pady=20)

        self.current_patient_labelframe.columnconfigure(0, weight=1)
        self.current_patient_labelframe.columnconfigure(1, weight=1)

        # Adding a label inside the labelframe
        self.current_patient_info_label = tk.Label(self.current_patient_labelframe, text=f"{self.link.listHead()}", font=("Times New Roman", 20))
        self.current_patient_info_label.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        # Adding the back button under the labelframe
        self.current_patient_back_button = tk.Button(self.current_patient_window, text="Back", font=("Times New Roman", 25, "bold"), command=self.current_patient_window.destroy)
        self.current_patient_back_button.pack(pady=20)

    def open_check_pending_list_window(self):
        self.check_pending_list = tk.Toplevel(self.root)
        self.check_pending_list.title("Pending Patients")
        self.check_pending_list.geometry("750x600")

        self.set_background(self.check_pending_list)

        self.check_pending_label = tk.Label(self.check_pending_list, text="Pending Patients", font=("Times New Roman", 45, "bold"))
        self.check_pending_label.pack(pady=20)
        
        #======= First Label Frame =========

        self.search_patient_labelframe = tk.LabelFrame(self.check_pending_list, text="Search Patient", font=("Times New Roman", 12, "bold"))
        self.search_patient_labelframe.pack(fill = 'x',padx=20, pady=20)

        self.searchPatientEntry = tk.Entry(self.search_patient_labelframe, font = ("Times New Roman", 15))
        self.searchPatientEntry.grid(row = 0, column = 0, padx = 15, pady = 5,sticky=tk.W+tk.E)

        self.button_serve_search_patient_confirm = tk.Button(self.search_patient_labelframe, text="Search", font=("Times New Roman", 12, "bold"), command = lambda: showSearchedPatient(self.searchPatientEntry.get())) 
        self.button_serve_search_patient_confirm.grid(row=0, column=1, padx=15, pady=5,sticky=tk.W+tk.E)

        self.search_patient_labelframe.columnconfigure(0, weight=1)
        self.search_patient_labelframe.columnconfigure(1, weight=1)

        #======= Second Label Frame =====

        self.check_pending_labelframe = tk.LabelFrame(self.check_pending_list, text="Pending Patients List", font=("Times New Roman", 15, "bold"))
        self.check_pending_labelframe.pack(fill='x', padx=20, pady=20)

        self.check_pending_labelframe.columnconfigure(0, weight=1)
        self.check_pending_labelframe.columnconfigure(1, weight=1)

        
        # Adding a label inside the labelframe
        self.pending_patient_info_label = tk.Label(self.check_pending_labelframe, text= "", font=("Times New Roman", 15))
        self.pending_patient_info_label.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        # Adding the back button under the labelframe
        self.pending_patient_back_button = tk.Button(self.check_pending_list, text="Back", font=("Times New Roman", 25, "bold"), command=self.check_pending_list.destroy)
        self.pending_patient_back_button.pack(pady=20)
        
        def showPatients(): #Configures the label to show all pending patients
            if not self.link.head:
                self.pending_patient_info_label.config(text= "There are no patients to serve yet")
                return
            nodes = self.link.displayPatients()
            self.pending_patient_info_label.config(text= "\n".join(map(str,nodes)))

        def showSearchedPatient(name):
            if self.link.search(name):
                self.pending_patient_info_label.config(text= f"{self.link.displayName(name)}")
            else:
                messagebox.showinfo("Patient Name Error", f"There is no patient named {name} in the facility")

        showPatients()

    def open_if_pending_full_window(self):
        self.pending_list_is_full = tk.Toplevel(self.root)
        self.pending_list_is_full.title("Patient Capacity")
        self.pending_list_is_full.geometry("750x570")

        self.set_background(self.pending_list_is_full)

        self.pending_is_full_label = tk.Label(self.pending_list_is_full, text="Patient Capacity", font=("Times New Roman", 40, "bold"))
        self.pending_is_full_label.pack(pady=20)

        self.pending_is_full_labelframe = tk.LabelFrame(self.pending_list_is_full, text="Current number of patients", font=("Times New Roman", 15, "bold"))
        self.pending_is_full_labelframe.pack(fill='x', padx=20, pady=20)

        self.pending_is_full_labelframe.columnconfigure(0, weight=1)
        self.pending_is_full_labelframe.columnconfigure(1, weight=1)

        textToDisplay = ""
        if self.link.length() < 10:
            textToDisplay = f'Current patient capacity is {self.link.length()}/10'
        else:
            textToDisplay = "The patient capacity is full"
        # Adding a label inside the labelframe
        self.pending_patient_info_label = tk.Label(self.pending_is_full_labelframe, text=textToDisplay, font=("Times New Roman", 20))
        self.pending_patient_info_label.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        # Adding the back button under the labelframe
        self.pending_patient_back_button = tk.Button(self.pending_list_is_full, text="Back", font=("Times New Roman", 25, "bold"), command=self.pending_list_is_full.destroy)
        self.pending_patient_back_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = Patient_Management_System(root)
    root.mainloop()
