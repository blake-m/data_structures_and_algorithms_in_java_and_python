""""""

from __future__ import annotations
from typing import Optional, Tuple

from stack_with_singly_linked_list import Stack
from tower_of_hanoi.disk import Disk


class Rod(Stack):
    members_dictionary = {}

    def __init__(self, name: str, first_element: Optional[Disk] = None) -> None:
        super().__init__(first_element)
        self.__name = name
        self.__add_self_to_members_dictionary()

    def __add_self_to_members_dictionary(self) -> None:
        Rod.members_dictionary[self.name] = self

    def push_disk_on_top(self, disk: Disk) -> bool:
        current_top_disk = self.peek_element_from_top()

        if disk.check_if_disk_below_exists_and_or_is_bigger(current_top_disk):
            super().push_element_on_top(disk)
            return True

        return False

    @property
    def name(self) -> str:
        return self.__name
