class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, val: int):
        node = Node(val)
        if self.front is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty.")
        elif self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty.")
        else:
            return self.front.val
