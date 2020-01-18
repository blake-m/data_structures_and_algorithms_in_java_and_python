"""

"""

from __future__ import annotations

from typing import Optional, Tuple

from tower_of_hanoi.disk import Disk
from tower_of_hanoi.rod import Rod


class Game:
    """

    Maximal number of disks is 12.

    The game has an option of "solving itself".
    """

    def __init__(self, gui_functions: dict) -> None:
        self.rod1 = Rod('Left')
        self.rod2 = Rod('Central')
        self.rod3 = Rod('Right')
        self.rods_dictionary = Rod.members_dictionary

        self.number_of_disks = gui_functions['difficulty']
        self.initialize_by_adding_first_disks_to_left_rod()

    def initialize_by_adding_first_disks_to_left_rod(self) -> None:
        """Pushes disks onto the left rod (number specified by player)."""
        list_of_disk_sizes = reversed(range(1, self.number_of_disks + 1))
        for disk_size in list_of_disk_sizes:
            self.rod1.push_disk_on_top(Disk(disk_size))

    def check_if_choice_in_available_choices(self, choice) -> bool:
        available_choices = list(self.rods_dictionary.keys())
        if choice in available_choices:
            return True
        return False

    def check_if_player_source_choice_correct(self, choice):
        # Zamien na try/except
        if self.check_if_choice_in_available_choices(choice):
            chosen_source_rod = self.rods_dictionary[choice]
            if not chosen_source_rod.is_empty():
                return True
        return False

    def check_if_player_destination_choice_correct(self, choice, disk_from_source_rod):
        if self.check_if_choice_in_available_choices(choice):
            chosen_destination_rod = self.rods_dictionary[choice]
            if chosen_destination_rod.is_empty():
                return True
            top_disk = chosen_destination_rod.peek_element_from_top()
            if top_disk.size < disk_from_source_rod.size:
                return False
            return True

    def get_source_rod(self):
        player_source_choice = input("Source: ")
        while not self.check_if_player_source_choice_correct(player_source_choice):
            player_source_choice = input("Source: ")
        print('Source: ', player_source_choice)
        return player_source_choice

    def get_destination_rod(self, disk_from_source_rod):
        player_destination_choice = input("Destination: ")
        while not self.check_if_player_destination_choice_correct(player_destination_choice, disk_from_source_rod):
            print("not correct!")
            player_destination_choice = input("Destination: ")
        print('Source: ', player_destination_choice)
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
