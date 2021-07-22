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
        # Print nothing if list is empty
        if self.head is None:
            return
        # Print head value
        current = self.head
        print(current.to_string())
        # Loop through the list printing the values for each node
        while current.has_next():
            current = current.next
            print(current.to_string())
        print("Finished printing")

    # Inserting functions
    def insert_start(self, value):
        new_start = Node(value)
        new_start.next = self.head
        self.head = new_start

    def insert_last(self, value):
        # If there is no head Node then new node becomes the head
        new_last = Node(value)
        if self.head is None:
            self.head = new_last
            return

        # Loop to the end of the list
        current = self.head
        while current.has_next():
            current = current.next
        
        # Assign the next item at the end of the list to the new Node
        current.next = new_last

    def insert(self, position, value):
        new_node = Node(value)

        # Case when position is start of the list
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            count = 1 # Position - 1

            # Loop to node before where we want to insert
            while count < position - 1:
                previous = previous.next
                count += 1

            # Assign current node 
            current = previous.next
            # Node to insert comes after the previous
            previous.next = new_node
            # Assign current node to the new nodes next
            new_node.next = current
    
    # Delete functions
    def delete_start(self):
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None

    def delete_last(self):
        if self.head is None or self.head.next is None:
            return self.head
        
        current = self.head
        previous = None

        # Loop through the linked list until the end
        while current.has_next():
            previous = current
            current = current.next
        
        # Breaks link between second last and last node
        previous.next = None
        return current

    def delete(self, position):
        if position == 1:
            self.head = self.head.next
        else:
            previous = self.head
            count = 1

            # Loop through to find position of node before target node
            while count < position - 1:
                previous = previous.next
                count += 1
            
            # Assign target node to current and skip its connection
            current = previous.next
            previous.next = current.next



# Instatiate LinkedList and Nodes containing integer values
myList = LinkedList()
# second = Node(8)
# third = Node(6)
# fourth = Node(4)
# fifth = Node(2)

# Add nodes to linked list in order
# myList.head = Node(10)
# myList.head.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth

# Create LinkedList using insert function
myList.insert(1, 12)
myList.insert(2, 10)
myList.insert(3, 8)
myList.insert(4, 6)
myList.insert(5, 4)

# Print all elements in the LinkedList

myList.print_list()

# Insert new element at the start of the list
myList.insert_start(14)

myList.print_list()

myList.delete_start()

myList.print_list()

myList.delete_last()

myList.print_list()

myList.delete(2)

myList.print_list()
