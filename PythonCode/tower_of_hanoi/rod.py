from __future__ import annotations
from typing import Optional, Tuple

from stack_with_singly_linked_list import Stack
from tower_of_hanoi.disk import Disk


class Rod(Stack):
    def __init__(self, name: str, first_element: Optional[Disk] = None) -> None:
        super().__init__(first_element)
        self.__name = name

    def push_disk_on_top(self, disk: Disk) -> bool:
        current_top_disk = self.peek_element_from_top()
        print('Top disk', current_top_disk)
        if disk.check_if_disk_can_be_moved_onto_specified_rod(current_top_disk):
            super().push_element_on_top(disk)
            return True
        return False

    @property
    def name(self):
        return self.__name
