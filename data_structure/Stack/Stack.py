import typing


class Stack:
    def __init__(self, size: int):
        self.stk = []
        self.size = size
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.size - 1
    
    def push(self, val: int):
        if self.isFull():
            raise Exception("Stack is full")
        else:
            self.stk.append(val)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            self.stk.pop()
            self.top -= 1

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.stk[self.top]
