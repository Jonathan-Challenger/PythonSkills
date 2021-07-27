"""
STACKS
"""


class Stack():
    def __init__(self):
        self.items = []

    # Check if stack is empty
    def isEmpty(self):
        return self.items == []

    # Add element to stack
    def push(self, item):
        self.items.insert(0, item)

    # Remove top item
    def pop(self):
        self.items.pop(0)

    # Check top item
    def peek(self):
        return self.items[0]

    # Size of stack
    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


myStack = Stack()
myStack.push("hello")
myStack.push(5)
myStack.push(True)
myStack.push(6.9)
myStack.push("World")
myStack.display()
myStack.pop()
myStack.display()
