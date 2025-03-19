class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next  # Save the next node
            curr.next = prev       # Reverse the current node's pointer
            prev = curr            # Move prev to the current node
            curr = next_node       # Move curr to the next node

        self.head = prev  # Update the head to the new front of the list

    def print_list(self):
        """Print the linked list."""
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Original linked list:")
ll.print_list()

ll.reverse()

print("Reversed linked list:")
ll.print_list()