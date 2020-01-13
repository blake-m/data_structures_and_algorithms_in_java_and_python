from singly_linked_list import SinglyLinkedList
from typing import Any


class Stack:
    def __init__(self, first_element: Any = None):
        self.stack_list = SinglyLinkedList()
        if first_element:
            self.stack_list.append(first_element)

    def get_size(self) -> int:
        return self.stack_list.size

    def is_empty(self) -> bool:
        return self.stack_list.size == 0

    def push_element_on_top(self, element: Any) -> None:
        self.stack_list.append(element)

    def pop_element_from_top(self) -> Any:
        return self.stack_list.remove_last()

    def peek_element_from_top(self) -> Any:
        return self.stack_list.get_position(self.stack_list.size)
