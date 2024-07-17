class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertEnd(self,newElement):
        newNode = Node(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = newNode
    
    def removeBeginning(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
    
    def printList(self):
        temp = self.head
        if(temp != None):
            print("\n", end=" ")
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
        else:
            print("\nThe list is empty.")

link = LinkedList()
link.insertEnd("1")
link.insertEnd("2")
link.printList()
link.removeBeginning()
link.printList()
