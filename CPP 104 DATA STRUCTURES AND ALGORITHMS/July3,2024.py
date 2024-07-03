class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self): # Check if the stack is empty
        return len(self.stack) == 0
    
    def push(self,item):#Add an item to the top of the stack
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)
    
#My code starts here
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(18)
stack.push(60)

#output area
print(stack)
#print(stack.peek())
#print(stack.__str__())
#print(stack.size())
#print(stack.pop())
#print(stack.peek())
'''for i in range(stack.size()):
    stack.pop()

print(stack.isEmpty())'''