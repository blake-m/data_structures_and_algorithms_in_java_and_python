from __future__ import annotations
from typing import Optional, Tuple


class Disk:
    def __init__(self, size: int) -> None:
        self.__size = size

    @property
    def size(self) -> int:
        return self.__size

    @staticmethod
    def check_if_there_is_disk_below(disk_below: Optional[Disk]) -> bool:
        if disk_below:
            return True
        return False

    def check_if_disk_below_is_bigger(self, disk_below: Optional[Disk]) -> bool:
        if disk_below.size > self.size:
            return True
        return False

    def check_if_disk_can_be_moved_onto_specified_rod(self, disk_below: Optional[Disk]) -> bool:
        if (not self.check_if_there_is_disk_below(disk_below)
                and self.check_if_disk_below_is_bigger(disk_below)):
            return True
        return False

    def __str__(self):
        return str(self.size)
