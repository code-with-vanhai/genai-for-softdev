class Node:
    """Class representing a single node in the linked list."""
    def __init__(self, data):
        self.data = data  # The data stored in the node
        self.next = None  # Pointer to the next node in the list

class LinkedList:
    """Class representing the linked list."""
    def __init__(self):
        self.head = None  # The head (first node) of the linked list

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None

    def append(self, data):
        """Add a new node to the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If the list is empty, set the new node as the head
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """Add a new node to the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first occurrence of a node with the specified data."""
        if self.head is None:
            return  # List is empty

        # If the head node is to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        # Search for the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:  # Node with data found
            current.next = current.next.next

    def display(self):
        """Print the linked list in a readable format."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()

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

    ll.delete(5)
    print("After deleting 5:")
    ll.display()

    ll.delete(30)
    print("After deleting 30:")
    ll.display()
