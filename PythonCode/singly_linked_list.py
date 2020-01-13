from __future__ import annotations
from typing import Any, Optional

NodeOrNone = Optional["SinglyLinkedList.__Node"]


class SinglyLinkedList:
    def __init__(self, first_element: Any = None):
        self.__size: int = 0
        self.__head: NodeOrNone = None
        self.__tail: NodeOrNone = None
        if first_element is not None:
            self.add_first(first_element)

    class __Node:
        def __init__(
                self,
                data: Optional[Any] = None,
                next_: NodeOrNone = None
        ) -> None:
            self.data = data
            self.next = next_

        def __str__(self) -> str:
            return str(self.data)

    @property
    def size(self) -> int:
        return self.__size

    def __len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.__size == 0

    def __add_to_empty_list(self, node: SinglyLinkedList.__Node) -> None:
        self.__head = node
        self.__tail = node

    def add_first(self, data: Any) -> None:
        node_to_add = SinglyLinkedList.__Node(data)
        if self.is_empty():
            self.__add_to_empty_list(node_to_add)
        else:
            node_to_add.next = self.__head
            self.__head = node_to_add
        self.__size += 1

    def add_last(self, data: Optional[Any]) -> None:
        node_to_add = SinglyLinkedList.__Node(data)
        if self.is_empty():
            self.__add_to_empty_list(node_to_add)
        else:
            self.__tail.next = node_to_add
            self.__tail = node_to_add
        self.__size += 1

    def clear(self) -> None:
        if not self.is_empty():
            while self.__head.next is not None:
                self.__head, self.__head = None, self.__head.next
            self.__head = None
            self.__tail = None
            self.__size = 0

    def __check_if_index_is_correct(self, index: int) -> None:
        if self.size == 0 and index == 0:
            raise IndexError("The list is empty")
        elif index < 0:
            raise IndexError("Index can't be lower than 0.")
        elif index >= self.size:
            raise IndexError("Index out of range.")

    def __get_node_at_index(self, index: int) -> SinglyLinkedList.__Node:
        self.__check_if_index_is_correct(index)

        current_node = self.__head
        for i in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any:
        node = self.__get_node_at_index(index)
        return node.data

    def check_first(self) -> Any:
        return self.__head.data

    def check_last(self) -> Any:
        return self.__tail.data

    def check_at_index(self, index: int) -> Any:
        return self[index]

    def __raise_index_error_if_list_is_empty(self) -> None:
        if self.is_empty():
            raise IndexError("The list is empty")

    def remove_first(self) -> Any:
        self.__raise_index_error_if_list_is_empty()

        removed_data = self.__head.data
        self.__head, self.__head = None, self.__head.next

        self.__size -= 1

        return removed_data

    def remove_last(self) -> Any:
        self.__raise_index_error_if_list_is_empty()

        removed_data = self.__tail.data
        if self.__size == 1:
            self.__head = self.__tail = None
        else:
            # In a singly linked list you don't know what the previous item was.
            # Therefore you need to traverse the whole list to get to the second to last item.
            second_to_last_node = self.__get_node_at_index(self.__size-2)
            self.__tail = second_to_last_node

        self.__size -= 1

        return removed_data

    def remove_at_index(self, index: int) -> Any:
        self.__raise_index_error_if_list_is_empty()
        self.__check_if_index_is_correct(index)

        removed_data = self[index]

        previous_node = self.__get_node_at_index(index-1)
        node_to_remove = previous_node.next
        previous_node.next = node_to_remove.next
        node_to_remove.next = None

        self.__size -= 1

        return removed_data

    def insert_item_at(self, data: Optional[Any], index: int) -> None:
        if index == 0:
            self.add_first(data)
        else:
            self.__check_if_index_is_correct(index)

            previous_node = self.__get_node_at_index(index-1)
            next_node = previous_node.next
            inserted_node = SinglyLinkedList.__Node(data, next_node)
            previous_node.next = inserted_node

        self.__size += 1

    def __iter__(self) -> SinglyLinkedList:
        if self.is_empty():
            raise StopIteration("Can't iterate over an empty list.")
        self.__current_node_at_iterator = None
        return self

    def __next__(self) -> Any:
        if not self.__current_node_at_iterator:
            self.__current_node_at_iterator = self.__head
            return self.__current_node_at_iterator.data

        if self.__current_node_at_iterator.next:
            self.__current_node_at_iterator = self.__current_node_at_iterator.next
            return self.__current_node_at_iterator.data

        raise StopIteration

    def __str__(self) -> str:
        return str([node_data for node_data in iter(self)])
