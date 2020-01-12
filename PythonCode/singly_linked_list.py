from typing import Any, Optional


class SinglyLinkedList:
    def __init__(self, first_element: Optional["SinglyLinkedList.Node"] = None):
        self.__size: int = 0
        self.__head: None
        self.__tail: None

    class Node:
        def __init__(
                self,
                data: Optional[Any] = None,
                next_: Optional["SinglyLinkedList.Node"] = None
        ) -> None:
            self.data: Any = data
            self.next: "SinglyLinkedList.Node" = next_

        def __str__(self):
            return str(self.data)

    @property
    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.__size == 0

    def add_first(self, data: Any):
        if self.is_empty():
            node_to_add = SinglyLinkedList.Node(data)
            self.__head = node_to_add
            self.__tail = node_to_add
        else:
            pass
        self.__size += 1
        pass

    def add_last(self):
        pass

    def clear(self):
        pass

    def __check_if_index_is_correct(self):
        pass

    def __get_node_at_index(self):
        pass

    def check_first(self):
        pass

    def check_last(self):
        pass

    def check_at_index(self):
        pass

    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def remove_at_index(self):
        pass

    def insert_object_at(self):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        pass