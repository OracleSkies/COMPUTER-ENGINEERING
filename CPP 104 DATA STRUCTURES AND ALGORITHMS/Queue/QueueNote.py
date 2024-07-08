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

# Example usage of the Queue class
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue) # Output: [1, 2, 3]
print(queue.dequeue()) # Output: 1
print(queue.front()) # Output: 2
print(queue.size()) # Output: 2