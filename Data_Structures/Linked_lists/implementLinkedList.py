"""
In this example I will be implementing a singly linked list 
with some basic methods such as search, length, insert, delete
"""

# Creating Node class which will be used in LinkedList
class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    #Function that returns the data of the current node
    def get_data(self):
        return self.data

    # Function that returns what the next node is
    def get_next(self):
        return self.next

    # Function gets the data of the next Node
    def get_next_data(self):
        return self.next.get_data()

    # Function to set next node
    def set_next(self, new_next):
        self.next = new_next

    # Function returning boolean depending on if current Node has a next Node
    def has_next(self):
        if self.get_next() is None:
            return False
        return True

    # Function that returns the data of the Node in a string
    def to_string(self):
        return "Node value: " + str(self.data)

# Create LinkedList class
class LinkedList():
    def __init__(self, head=None):
        self.head = head
    
    # Function that prints all the values in the linkedlist
    def print_list(self):
        print("Printing list..........")
        if self.head is None:
            return
        current = self.head
        print(current.to_string())
        while current.has_next():
            current = current.get_next()
            print(current.to_string())
        print("Finished printing")

    # Inserting functions
    def insert_start(self, value):
        new_start = Node(value)
        new_start.next = self.head
        self.head = new_start

    def insert_last(self, value):
        new_last = Node(value)
        if self.head is None:
            self.head = new_last
            return

        current = self.head
        while current.has_next():
            current = current.next
        
        current.next = new_last


# Instatiate LinkedList and Nodes containing integer values
myList = LinkedList()
second = Node(8)
third = Node(6)
fourth = Node(4)
fifth = Node(2)

# Add nodes to linked list in order
myList.head = Node(10)
myList.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Print all elements in the LinkedList

myList.print_list()

# Insert new element at the start of the list

myList.insert_end(1)

myList.print_list()