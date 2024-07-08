class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
    # Check if the queue is empty
        return len(self.queue) == 0

    def enqueue(self, item):
    # Add an item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
    # Remove and return the item from the front of the queue
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def front(self):
    # Return the item at the front of the queue without removing it
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.queue[0]

    def size(self):
    # Return the number of items in the queue
        return len(self.queue)

    def __str__(self):
    # Return a string representation of the queue
        return str(self.queue)
    
queue = Queue()

print("WELCOME TO THE CUSTOMER SERVICE SOFTWARE")

while True:
    #take customer name? and add to queue
    print()
    print("1. New Customer")
    print("2. Check current customer in transaction")
    print("3. Check the current queue")
    print("4. Complete transaction of the current customer")
    print("5. Exit")
    print()
    userInput = int(input("Please enter the number of the action you want to do: "))
    
    match userInput:
        case 1:
            nameInput = input("Please enter your name: ")
            queue.enqueue(nameInput)
            print()
            print(f"Welcome {nameInput}!\nYou are now added to the queue.\nPlease be patient while making your transaction")
            print()
        case 2:
            if queue.is_empty():
                print("There are no customers in queue")
                print()
            else:
                print(f"The current customer is {queue.front()}")
                print()
        case 3:
            #loops the queue
            print()
            print(f"The current number of customers in queue: {queue.size()} ")
            print("These are the current customers in queue")
            for name in queue.queue:
                print(name)
        case 4:
            if queue.is_empty():
                print("There are no customers in queue")
                print()
            else:
                print(f"{queue.front()} is now done with the transaction.\nThank you and come again!")
                print()
                queue.dequeue()
        case 5:
            print("Thank you for using the software")
            print()
            break
        case _:
            print("Invalid input. Enter the number corresponding to your desired action.")

        

    


    
