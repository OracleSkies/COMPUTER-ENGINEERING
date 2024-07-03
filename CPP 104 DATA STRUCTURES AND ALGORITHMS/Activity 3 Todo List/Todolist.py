class Todo:
    def __init__(self):
        self.tasks = []
    
    def isEmpty(self): # Check if the.tasks is empty
        return len(self.tasks) == 0
    
    def push(self,item):#Add an item to the top of the.tasks
        self.tasks.append(item)
        print(f"{item} added successfully to your to do list")

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from an empty.tasks")
        return self.tasks.pop()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from an empty.tasks")
        return self.tasks[-1]
    
    def size(self):
        return len(self.tasks)
    

print("TO DO LIST")
print()
todo = Todo()
while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View current task")
    print("4. Display number of task")
    print("5. Display all tasks")
    print("6. Quit")
    userInput = int(input("Please enter the number of the action you want to do: "))
    print()

    match userInput:
        case 1:
            taskInput = input("Input task: ")
            todo.push(taskInput)
            print()
        case 2:
            print(f"{todo.pop()} removed from the to do list")
            print()
        case 3:
            print(f"Your current task is {todo.peek()}")
            print()
        case 4:
            print(f"The current number of your task is {todo.size()}")
            print()
        case 5:
            print("This is your current to do list")
            print(todo.tasks)
            print()
        case 6:
            print("Thank you for using the to do list")
            break
        case _:
            print("Invalid input. It must be a number")
            print()