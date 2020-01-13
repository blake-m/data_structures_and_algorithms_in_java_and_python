import os

from singly_linked_list import SinglyLinkedList
from typing import Any


class Stack:
    def __init__(self, first_element: Any = None):
        self.__stack_list = SinglyLinkedList()
        if first_element:
            self.__stack_list.add_last(first_element)

    def get_size(self) -> int:
        return self.__stack_list.size

    def is_empty(self) -> bool:
        return self.__stack_list.size == 0

    def push_element_on_top(self, element: Any) -> None:
        self.__stack_list.add_last(element)

    def pop_element_from_top(self) -> Any:
        return self.__stack_list.remove_last()

    def peek_element_from_top(self) -> Any:
        return self.__stack_list.check_last()

    def __len__(self) -> int:
        return len(self.__stack_list)

    def __str__(self) -> str:
        return str(self.__stack_list)