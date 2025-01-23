class Node:
    """Class representing a single node in the linked list."""
    def __init__(self, data):
        self.data = data  # The data stored in the node
        self.next = None  # Pointer to the next node in the list

class LinkedList:
    """Class representing the linked list."""
    def __init__(self, max_size=None):
        self.head = None  # The head (first node) of the linked list
        self.size = 0  # Current size of the linked list
        self.max_size = max_size  # Maximum allowed size of the linked list

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def is_full(self):
        """Check if the linked list has reached its maximum size."""
        return self.max_size is not None and self.size >= self.max_size

    def append(self, data):
        """Add a new node to the end of the linked list."""
        if self.is_full():
            raise OverflowError("Linked list is full. Cannot append new elements.")

        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If the list is empty, set the new node as the head
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node

        self.size += 1

    def prepend(self, data):
        """Add a new node to the beginning of the linked list."""
        if self.is_full():
            raise OverflowError("Linked list is full. Cannot prepend new elements.")

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete(self, data):
        """Delete the first occurrence of a node with the specified data."""
        if self.head is None:
            return  # List is empty

        # If the head node is to be deleted
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return

        # Search for the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:  # Node with data found
            current.next = current.next.next
            self.size -= 1

    def display(self):
        """Print the linked list in a readable format."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def clear(self):
        """Clear the entire linked list."""
        self.head = None
        self.size = 0

# Example usage
if __name__ == "__main__":
    ll = LinkedList(max_size=5)  # Set a maximum size for the linked list

    try:
        ll.append(10)
        ll.append(20)
        ll.append(30)
        print("Initial list:")
        ll.display()

        ll.prepend(5)
        print("After prepending 5:")
        ll.display()

        ll.delete(20)
        print("After deleting 20:")
        ll.display()

        ll.append(40)
        ll.append(50)
        print("After adding more elements:")
        ll.display()

        ll.append(60)  # This should raise an OverflowError
    except OverflowError as e:
        print(e)

    print("Final list:")
    ll.display()
