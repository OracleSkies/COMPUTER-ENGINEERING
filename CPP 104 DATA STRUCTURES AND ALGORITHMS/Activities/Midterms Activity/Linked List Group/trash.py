import tkinter as tk

# Define the Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display_list(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes

# Function to update the label text
def update_label():
    nodes = linked_list.display_list()
    label.config(text="Linked List: " + " -> ".join(map(str, nodes)))

# Create a linked list instance
linked_list = LinkedList()

# Example: Append nodes to the linked list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Create the GUI window
window = tk.Tk()
window.title("Linked List Display")

# Create a label to display the linked list
label = tk.Label(window, text="", font=("Arial", 12))
label.pack(padx=20, pady=20)

# Button to update the label text
update_button = tk.Button(window, text="Update List", command=update_label)
update_button.pack()

# Initial update of the label
update_label()

# Run the main GUI loop
window.mainloop()
