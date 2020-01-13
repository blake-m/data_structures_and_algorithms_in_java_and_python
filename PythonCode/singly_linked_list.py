from typing import Any, Optional

NodeOrNone = Optional["SinglyLinkedList.Node"]

class SinglyLinkedList:
    def __init__(self, first_element: NodeOrNone = None):
        self.__size: int = 0
        self.__head: NodeOrNone = None
        self.__tail: NodeOrNone = None

    class Node:
        def __init__(
                self,
                data: Optional[Any] = None,
                next_: NodeOrNone = None
        ) -> None:
            self.data = data
            self.next = next_

        def __str__(self):
            return str(self.data)

    @property
    def size(self) -> int:
        return self.__size

    def ___len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.__size == 0

    def __add_to_empty_list(self, node: "SinglyLinkedList.Node"):
        self.__head = node
        self.__tail = node

    def add_first(self, data: Any):
        node_to_add = SinglyLinkedList.Node(data)
        if self.is_empty():
            self.__add_to_empty_list(node_to_add)
        else:
            node_to_add.next = self.__head
            self.__head = node_to_add
        self.__size += 1

    def add_last(self, data: Optional[Any]):
        node_to_add = SinglyLinkedList.Node(data)
        if self.is_empty():
            self.__add_to_empty_list(node_to_add)
        else:
            self.__tail.next = node_to_add
            self.__tail = node_to_add
        self.__size += 1

    def clear(self):
        if not self.is_empty():
            while self.__head.next is not None:
                self.__head, self.__head = None, self.__head.next
            self.__head = None
            self.__tail = None
            self.__size = 0

    def __check_if_index_is_correct(self, index: int):
        if self.size == 0 and index == 0:
            raise IndexError("The list is empty")
        elif index < 0:
            raise IndexError("Index can't be lower than 0.")
        elif index >= self.size:
            raise IndexError("Index out of range.")

    def __getitem__(self, index: int):
        self.__check_if_index_is_correct(index)
        current_node = self.__head
        for i in range(index):
            current_node = current_node.next
        return current_node.data

    def check_first(self):
        return self.__head

    def check_last(self):
        return self.__head

    def check_at_index(self, index: int):
        return self[index]

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
