"""This module contains a Rod class for Tower of Hanoi game."""
from __future__ import annotations
from typing import Optional, Tuple

from stack_with_singly_linked_list import Stack
from tower_of_hanoi.disk import Disk


class Rod(Stack):
    members_dictionary = {}

    def __init__(
            self,
            name: str,
            first_element: Optional[Disk] = None) -> None:
        """Creates a Rod class object.

        Rod is based on a stack Data Structure. If first_element argument is
        provided, a Rod already containing 1 element (a Disk) is created).

        Every time a Rod object is created it is also added to a class
        attribute, a members_dictionary, through which a user can access all
        the rods by specifying their name as a key. In Tower of Hanoi game
        there are always 3 rods with the following names: 'left', 'central',
        'right'.
        """
        super().__init__(first_element)
        self.__name = name
        self.__add_self_to_members_dictionary()

    def __add_self_to_members_dictionary(self) -> None:
        """Adds the given instance of a Rod class to the class attribute
        dictionary. Key is the name of the Rod, value is the Rod itself."""
        Rod.members_dictionary[self.name] = self

    @property
    def name(self) -> str:
        return self.__name

    def push_disk_on_top(self, disk: Disk) -> bool:
        """Tries to push a given disk at the top of the Rod Disks Stack.

        If successful, returns True. Else, returns False."""
        current_top_disk = self.peek_element_from_top()

        if disk.check_if_target_disk_below_exists_and_is_bigger(current_top_disk):
            self.push_element_on_top(disk)
            return True

        return False
