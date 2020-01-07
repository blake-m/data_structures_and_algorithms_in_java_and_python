# Singly Linked List

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        if self.head:
            self.size = 1

    def append(self, new_element):
        current_head = self.head
        if self.head:
            while current_head.next:
                current_head = current_head.next
            current_head.next = new_element
        else:
            self.head = new_element
        self.size += 1

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position < 1:
            return None
        current_element = self.head
        current_position = 1
        try:
            while current_position < position:
                current_element = current_element.next
                current_position += 1
            return current_element
        except Exception as e:
            print(e)
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current_element_at_given_position = self.get_position(position)
        previous_element = self.get_position(position - 1)
        new_element.next = current_element_at_given_position
        if previous_element:
            previous_element.next = new_element
        else:
            self.head = new_element
        self.size += 1

    def delete(self, value):
        """Delete the first node with a given value."""
        current_element = self.head
        for i in range(1, self.size + 1):
            if current_element.value == value:
                next_element = current_element.next
                previous_element = self.get_position(i - 1)
                if previous_element:
                    previous_element.next = next_element
                else:
                    self.head = next_element
                break
            current_element = current_element.next
        self.size -= 1


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
