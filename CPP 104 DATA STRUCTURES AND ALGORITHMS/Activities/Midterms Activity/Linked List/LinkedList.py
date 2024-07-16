class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(Node):
    def __init__(self):
        self.head = None

    def insertBeginning(self,newElement):
        newNode = Node(newElement)
        newNode.next = self.head
        self.head = newNode

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

    def insertMiddle(self,newElement,position):
        newNode = Node(newElement)
        if(position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1):
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, position-1):
                if(temp != None):
                    temp = temp.next
            if(temp != None):
                newNode.next = temp.next
                temp.next = newNode
            else:
                print("\nThe previous node is null.")
    def removeBeginning(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
            
    def removeEnd(self):
        if(self.head != None):
            if(self.head.next == None):
                self.head = None
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
                lastNode = temp.next
                temp.next = None
                lastNode = None
                
    def removeMiddle(self,position):
        if(position < 1):
            print("\nposition should be >=1.")
        elif(position == 1 and self.head != None):
            nodeToDelete = self.head
            self.head = self.head.next
            nodeToDelete = None
        else:
            temp = self.head
            for i in range(1, position-1):
                if (temp != None):
                    temp = temp.next
            if(temp != None and temp.next != None):
                nodeToDelete = temp.next
                temp.next = temp.next.next
                NodeToDelete = None
            else:
                print("\nThe node is already null.")

    def print(self):
        temp = self.head
        if(temp != None):
            print("\n", end=" ")
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
        else:
            print("\nThe list is empty.")