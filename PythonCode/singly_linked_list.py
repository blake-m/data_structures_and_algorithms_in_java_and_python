# Basic implementation of Singly Linked List with head tracking only
# - this is not a complete implementation - just basic methods
# - this implementation contains unittests


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        if self.head:
            self.size = 1
        else:
            self.size = 0

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

    def remove_last(self):
        """Delete the last node and return its value."""
        value_to_return = None
        previous_element = None
        current_element = self.head
        current_position = 1

        while current_position < self.size:
            previous_element = current_element
            current_element = current_element.next
            current_position += 1

        value_to_return = current_element.value
        current_element = None
        if previous_element:
            previous_element.next = None
        else:
            self.head = None
        self.size -= 1

        return value_to_return
