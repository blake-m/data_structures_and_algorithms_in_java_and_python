"""My implementation of Tower of Hanoi in Python.

This algorithm is based on my own implementation of Stack (which in turn was
built on top of my implementation of singly linked list).

Rules (copied from: https://www.geeksforgeeks.org/):
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
The objective of the puzzle is to move the entire stack to another rod,
obeying the following simple rules:
    1) Only one disk can be moved at a time.
    2) Each move consists of taking the upper disk from one of the stacks
    and placing it on top of another stack i.e. a disk can only be moved
    if it is the uppermost disk on a stack.
    3) No disk may be placed on top of a smaller disk.
"""
from __future__ import annotations

from typing import Optional, Tuple
from stack_with_singly_linked_list import Stack


class Disk:
    def __init__(self, size: int) -> None:
        self.__size = size

    @property
    def size(self) -> int:
        return self.__size

    def check_if_size_of_disk_below_is_correct(self, disk_below: Optional[Disk]) -> bool:
        if not disk_below:  # Evaluates to True if there's no disk below
            return True
        if disk_below.size > self.size:
            return True
        return False

    def __str__(self):
        return str(self.size)


class Rod(Stack):
    def __init__(self, name: str, first_element: Optional[Disk] = None) -> None:
        super().__init__(first_element)
        self.__name = name

    def push_disk_on_top(self, disk: Disk) -> bool:
        current_top_disk = self.peek_element_from_top()
        print('Top disk', current_top_disk)
        if disk.check_if_size_of_disk_below_is_correct(current_top_disk):
            super().push_element_on_top(disk)
            return True
        return False

    @property
    def name(self):
        return self.__name




class Game:
    """

    Maximal number of disks is 12.

    The game has an option of "solving itself".
    """

    def __init__(self, number_of_disks: int = 5) -> None:
        self.rod1 = Rod('Left Rod')
        self.rod2 = Rod('Central Rod')
        self.rod3 = Rod('Right Rod')
        self.rods_dictionary = {
            'Left': self.rod1,
            'Central': self.rod2,
            'Right': self.rod3,
        }
        self.number_of_disks = number_of_disks
        self.initialize_by_adding_first_disks_to_left_rod()

    def initialize_by_adding_first_disks_to_left_rod(self) -> None:
        """Pushes disks onto the left rod (number specified by player)."""
        list_of_disk_sizes = reversed(range(1, self.number_of_disks + 1))
        for disk_size in list_of_disk_sizes:
            print('lol')
            print(disk_size)
            print(self.rod1.push_disk_on_top(Disk(disk_size)))
        print(self.rod1.get_size())

    def check_if_choice_in_available_choices(self, choice) -> bool:
        available_choices = list(self.rods_dictionary.keys())
        if choice in available_choices:
            print("Good, it's in available_choices")
            return True
        return False

    def check_if_player_source_choice_correct(self, choice):
        # Zamien na try/except
        if self.check_if_choice_in_available_choices(choice):
            chosen_source_rod = self.rods_dictionary[choice]
            print(chosen_source_rod.get_size())
            if not chosen_source_rod.is_empty():
                return True
        return False

    def check_if_player_destination_choice_correct(self, choice, disk_from_source_rod):
        if self.check_if_choice_in_available_choices(choice):
            chosen_destination_rod = self.rods_dictionary[choice]
            if chosen_destination_rod.is_empty():
                return True
            top_disk = chosen_destination_rod.peek_element_from_top()
            print(disk_from_source_rod.size)
            print(top_disk.size)
            if top_disk.size < disk_from_source_rod.size:
                return False
            return True

    def get_source_rod(self):
        player_source_choice = input("Prompt: ")
        while not self.check_if_player_source_choice_correct(player_source_choice):
            print("not correct!")
            player_source_choice = input("Prompt: ")
        print('Source: ', player_source_choice)
        print("correct")
        return player_source_choice

    def get_destination_rod(self, disk_from_source_rod):
        player_destination_choice = input("Prompt: ")
        while not self.check_if_player_destination_choice_correct(player_destination_choice, disk_from_source_rod):
            print("not correct!")
            player_destination_choice = input("Prompt: ")
        print('Source: ', player_destination_choice)
        print("correct")
        return player_destination_choice

    def ask_player_for_destination_and_source_rods(self) -> Tuple[str, str]:
        choice_source_rod = self.get_source_rod()
        disk_from_source_rod = self.rods_dictionary[choice_source_rod].peek_element_from_top()
        choice_destination_rod = self.get_destination_rod(disk_from_source_rod)
        if choice_source_rod != choice_destination_rod:
            return choice_source_rod, choice_destination_rod
        print("You can't choose the same rod twice. Choose again! ;)")
        self.ask_player_for_destination_and_source_rods()

    def change_disks_location_from_one_rod_to_another(self, source: str, destination: str):
        """Takes disk from one rod and puts it onto another."""
        source_rod = self.rods_dictionary[source]
        destination_rod = self.rods_dictionary[destination]

        chosen_disk = source_rod.pop_element_from_top()
        destination_rod.push_disk_on_top(chosen_disk)

    def make_move(self):
        choice_source_rod, choice_destination_rod = self.ask_player_for_destination_and_source_rods()
        self.change_disks_location_from_one_rod_to_another(choice_source_rod, choice_destination_rod)

    def check_if_right_rod_full_and_others_empty(self):
        if (self.rod3.get_size() == self.number_of_disks
                and self.rod1.is_empty()
                and self.rod2.is_empty()):
            return True
        return False


class TextGUI:
    def __init__(self, game):
        self.game = game

    def print_current_state(self):
        print('\n' * 100)
        for rod in self.game.rods_dictionary.values():
            if rod.is_empty():
                print(rod.name, ": Empty")
            else:
                disks_representations = [disk.size*'@' for disk in iter(rod)]
                print(rod.name, ": ", disks_representations)


def main():
    # TODO: you implemented __iter__ in stack - test it
    # TODO: When you Move object from 1 rod to another it seems to get copied, not moved - fix
    game = Game(10)
    gui = TextGUI(game)
    while not game.check_if_right_rod_full_and_others_empty():
        gui.print_current_state()
        game.make_move()
    print("congrats")


if __name__ == "__main__":
    main()
