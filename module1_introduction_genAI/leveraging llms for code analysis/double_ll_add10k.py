import threading

class Node:
    """Class representing a single node in the doubly linked list."""
    def __init__(self, data):
        if not isinstance(data, (int, str)):
            raise TypeError("Only integers and strings are allowed")
        self.data = data  # The data stored in the node
        self.next = None  # Pointer to the next node in the list
        self.prev = None  # Pointer to the previous node in the list

class DoublyLinkedList:
    """Class representing the doubly linked list with security measures."""
    def __init__(self, max_size=None):
        self.head = None  # The head (first node) of the linked list
        self.tail = None  # The tail (last node) of the linked list
        self.size = 0  # Current size of the linked list
        self.max_size = max_size  # Maximum allowed size of the linked list
        self.lock = threading.Lock()  # Thread safety lock

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def is_full(self):
        """Check if the linked list has reached its maximum size."""
        return self.max_size is not None and self.size >= self.max_size

    def append(self, data):
        """Add a new node to the end of the linked list with security checks."""
        if not isinstance(data, (int, str)):
            raise TypeError("Only integers and strings are allowed")
        if len(str(data)) > 1000:
            raise ValueError("Data size exceeds maximum limit")
        with self.lock:
            if self.is_full():
                raise OverflowError("Doubly linked list is full. Cannot append new elements.")
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            self.size += 1

    def prepend(self, data):
        """Add a new node to the beginning of the linked list with security checks."""
        if not isinstance(data, (int, str)):
            raise TypeError("Only integers and strings are allowed")
        if len(str(data)) > 1000:
            raise ValueError("Data size exceeds maximum limit")
        with self.lock:
            if self.is_full():
                raise OverflowError("Doubly linked list is full. Cannot prepend new elements.")
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self.size += 1

    def delete(self, data):
        """Delete the first occurrence of a node with the specified data safely."""
        with self.lock:
            if self.head is None:
                return  # List is empty
            current = self.head
            while current and current.data != data:
                current = current.next
            if current:  # Node with data found
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1

    def display(self):
        """Print the doubly linked list in a readable format."""
        with self.lock:
            current = self.head
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")

    def display_reverse(self):
        """Print the doubly linked list in reverse order."""
        with self.lock:
            current = self.tail
            while current:
                print(current.data, end=" <-> ")
                current = current.prev
            print("None")

    def clear(self):
        """Clear the entire linked list."""
        with self.lock:
            self.head = None
            self.tail = None
            self.size = 0

# Sample usage
import time

dll = DoublyLinkedList()

start_time = time.time()
for i in range(10000):
    dll.append(i)
end_time = time.time()

print("Time taken to append 10,000 items:", end_time - start_time, "seconds")
