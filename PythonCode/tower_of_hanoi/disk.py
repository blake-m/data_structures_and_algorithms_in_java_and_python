"""This module contains a Disk class for Tower of Hanoi game."""
from __future__ import annotations
from typing import Optional, Tuple


class Disk:
    def __init__(self, size: int) -> None:
        self.__size = size

    @property
    def size(self) -> int:
        return self.__size

    def check_if_target_disk_below_exists_and_is_bigger(
            self, disk_below: Optional[Disk]) -> bool:
        """Returns True if disk can be moved onto a specified rod.

        Takes a disk from a rod to which the current disk is supposed to be
        moved to. 3 Cases here:
        1.  Checks if this disk exists. If it doesn't - returns True -
            in Tower of Hanoi disks can be always moved to empty rods.
        2.  If the disk below exists and is bigger - returns True.
        3.  If the disk below exists and is smaller - returns False.

        Args:
            disk_below: peeked from the rod onto which the current disk
                is supposed to be moved to.
        """
        try:
            if disk_below.size > self.size:
                return True
            return False
        except AttributeError:
            return True   # Disk below doesn't exist

    def __str__(self) -> str:
        return str(self.size)
