# Queue Implementation in Python (Array)
class Queue:
    def __init__(self, size):
        self.capacity = size
        self.arr = [None] * size #create an array of given size: 
        #* size will create a list of None values with the specified size
        self.front = self.rear = -1#defining front and rear pointers to -1, indicating an empty queue
    
    # Add element to the rear (enqueue)
    def enqueue(self, item):
        if (self.rear + 1) % self.capacity == self.front:
            #Ex: capacity = 5, front = 0, rear = 4
            # (rear + 1) % capacity = (4 + 1) % 5 = 0, which is equal to front, indicating the queue is full
            #checking if the queue is full by comparing the next position of rear with front
            print("Queue Overflow")
            return
        if self.front == -1:# If the queue is empty, set front and rear to 0
            self.front = self.rear = 0
        else:# If the queue is not empty, move rear to the next position in a circular manner
            #ex: if rear is at the last index of the array, it wraps around to the beginning (index 0)
            self.rear = (self.rear + 1) % self.capacity
            #ex: if rear is at index 4 (last index) and capacity is 5, (4 + 1) % 5 = 0, 
            # so rear wraps around to the start of the array
        self.arr[self.rear] = item# Add the new item to the position pointed by rear in the array
        
    # Remove element from front (dequeue)
    def dequeue(self):
        if self.front == -1:# If the queue is empty, return an error message
            print("Queue Underflow")
            return -1
        item = self.arr[self.front]
        if self.front == self.rear:# If the queue has only one element, reset front and rear to -1 (empty state)
            self.front = self.rear = -1
        else:# If the queue has more than one element, move front to the next position in a circular manner
            self.front = (self.front + 1) % self.capacity
            #ex: if front is at index 4 (last index) and capacity is 5, (4 + 1) % 5 = 0, 
            # so front wraps around to the start of the array
        return item

# Usage Example
q = Queue(5)
q.enqueue(10)
print("Enqueue: 10")
q.enqueue(20)
print("Enqueue: 20")
q.enqueue(30)
print("Enqueue: 30")
print("Dequeue:", q.dequeue())  # 10
print("Dequeue:", q.dequeue())  # 20