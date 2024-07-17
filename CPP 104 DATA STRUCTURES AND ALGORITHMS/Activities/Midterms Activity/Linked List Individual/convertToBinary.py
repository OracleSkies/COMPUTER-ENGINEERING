class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self): #checks if list is empty
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
    
    def delete_node_at_position(self, position): #deletes node using index/position
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

    def print_list(self): #prints the list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def clearList(self): #clears the list
        while not self.is_empty():
            self.delete_node_at_position(0)
    
    def convertToBinary(self,num): #converts num to binary
        binary = bin(num)[2:]
        for char in binary:
            self.append(char)


link = LinkedList()
while True:
    userInput = int(input("Please enter a number to convert to binary: "))
    print()
    link.convertToBinary(userInput)
    link.print_list()
    link.clearList()
    print()
    userContinue = input("Do you want to continue? Y/N: ")
    match userContinue.lower():
        case "y":
            pass
        case "n":
            print()
            print("Thank you")
            break
        case _:
            print()
            print("Invalid Input")
