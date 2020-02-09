"""This module implements all backend game mechanics.

Rules of the game are specified in __main__.py

Different kinds of GUIs can be connected with this module via a dictionary
passed as a first __init__ argument 'gui_functions'. Having a dictionary
with gui_functions lets backend steer what is displayed and, as said,
allows other GUIs to be used.

List of functions that need to be implemented in a GUI:
# TODO(blake) make a list of these

"""

from __future__ import annotations

from typing import Optional, Tuple, List

import time

from tower_of_hanoi.disk import Disk
from tower_of_hanoi.rod import Rod


class Game:
    """Implements all game mechanics.

    Maximal number of disks allowed is 12.

    The game has an option of "solving itself". For more details look at
    'self.start_game()' and 'self.auto_solve_algorithm' methods.
    """
    def __init__(self, gui_functions: dict) -> None:
        self.rod1 = Rod('left')
        self.rod2 = Rod('central')
        self.rod3 = Rod('right')
        self.rods_dictionary = Rod.members_dictionary

        # To call a function retrieve it from this dictionary
        # by specifying a key and simply call it.
        self.gui_funcs = gui_functions

        # Waiting time before self-solving algorithms steps.
        self.wait_time = self.gui_funcs['get_wait_time']()

        self.number_of_disks = self.gui_funcs['difficulty']()
        self.initialize_by_adding_first_disks_to_left_rod()

    def initialize_by_adding_first_disks_to_left_rod(self) -> None:
        """Pushes n disks onto the left rod.

        n is taken from self.number_of_disks which in turn is specified
        by player via GUI.
        """
        list_of_disk_sizes = reversed(range(1, self.number_of_disks + 1))
        for disk_size in list_of_disk_sizes:
            self.rod1.push_disk_on_top(Disk(disk_size))

    @staticmethod
    def get_full_choice_string_from_1_letter_choice(choice: str) -> str:
        """Recreates long versions of allowed choices from 3 letters.

        Also: makes sure the string is in lower case.

        If long version of choice was provided or the string with choice does
        not include a proper short version or not a proper choice at all:
        the unmodified choice is simply returned for further verification.

        Arguments:
            choice: choice of either source or destination rod taken from
                users input.
        """
        choice = choice.lower()
        if choice == 'l':
            return 'left'
        elif choice == 'r':
            return 'right'
        elif choice == 'c':
            return 'central'
        return choice

    def check_if_choice_in_available_choices(self, choice: str) -> bool:
        available_choices = list(self.rods_dictionary.keys())
        if choice in available_choices:
            return True
        return False

    def check_if_player_source_choice_correct(self, choice: str) -> bool:
        if self.check_if_choice_in_available_choices(choice):
            chosen_source_rod = self.rods_dictionary[choice]
            if not chosen_source_rod.is_empty():
                return True
        return False

    def check_if_player_destination_choice_correct(
            self, choice: str, disk_from_source_rod: Disk) -> bool:
        """Returns True if disk can be moved.

        Uses previously specified functions to see if the player's choice
        (retrieved from input) is in allowed choices. If it is, takes a rod
        chosen by the player and retrieves its 'top_disk'.

        Next it compares the retrieved 'top_disk' with the
        'disk_from_source_rod' and if the latter can be placed on the former
        returns True. Otherwise it returns False.
        """
        if self.check_if_choice_in_available_choices(choice):
            chosen_destination_rod = self.rods_dictionary[choice]

            top_disk = chosen_destination_rod.peek_element_from_top()

            return disk_from_source_rod.\
                check_if_target_disk_below_exists_and_is_bigger(top_disk)

    def get_source_rod(self) -> str:
        """Returns the name of the rod from which the player
        wants to retrieve a Disk.
        """
        player_source_choice =\
            self.get_full_choice_string_from_1_letter_choice(
                input("Source: "))

        while not self.check_if_player_source_choice_correct(player_source_choice):
            self.gui_funcs['source_choose_again']()
            player_source_choice = \
                self.get_full_choice_string_from_1_letter_choice(
                    input("Source: "))

        self.gui_funcs['show_source_choice'](player_source_choice)

        return player_source_choice

    def get_destination_rod(self, disk_from_source_rod: Disk) -> str:
        """Returns the name of the rod to which the player
        wants to push their chosen Disk.
        """
        player_destination_choice =\
            self.get_full_choice_string_from_1_letter_choice(
                input("Destination: "))

        while not self.check_if_player_destination_choice_correct(
                player_destination_choice, disk_from_source_rod):
            self.gui_funcs['destination_choose_again']()
            player_destination_choice = \
                self.get_full_choice_string_from_1_letter_choice(
                    input("Destination: "))

        self.gui_funcs['show_destination_choice'](player_destination_choice)

        return player_destination_choice

    def ask_player_for_destination_and_source_rods(self) -> Tuple[str, str]:
        choice_source_rod = self.get_source_rod()
        disk_from_source_rod = self.rods_dictionary[
            choice_source_rod].peek_element_from_top()
        choice_destination_rod = self.get_destination_rod(disk_from_source_rod)

        # TODO(blake): make sure this recursion is not needed and delete it if so.
        #  Otherwise delete the print and use gui func instead.
        if choice_source_rod != choice_destination_rod:
            return choice_source_rod, choice_destination_rod

        print("You can't choose the same rod twice. Choose again! ;)")
        self.ask_player_for_destination_and_source_rods()

    def change_disks_location_from_one_rod_to_another(
            self, source: str, destination: str
    ) -> None:
        """Takes disk from one rod and puts it onto another."""
        source_rod = self.rods_dictionary[source]
        destination_rod = self.rods_dictionary[destination]

        chosen_disk = source_rod.pop_element_from_top()
        destination_rod.push_disk_on_top(chosen_disk)

    def make_move(self) -> None:
        """Allows the player to make a move.

        On the way it uses other functions to check the validity of the move.
        """
        choice_source_rod, choice_destination_rod = \
            self.ask_player_for_destination_and_source_rods()

        self.change_disks_location_from_one_rod_to_another(
            choice_source_rod, choice_destination_rod)

    def check_if_right_rod_full_and_others_empty(self) -> bool:
        """This is a winning condition. Returns True if game is finished."""
        if (self.rod3.get_size() == self.number_of_disks
                and self.rod1.is_empty()
                and self.rod2.is_empty()):
            return True
        return False

    def make_and_show_1_move(self, source: str, destination: str) -> None:
        """Allows the algorithm to make 1 move.

        Based on input moves 1 disk from 1 rod to another. Validity checks
        are not done on the way as the algorithm itself assures the validity
        of choices. After each move there's a wait time specified by player
        by interaction with a GUI. This method takes it from self.wait_time
        attribute.

        After the move is made asks GUI to show the current state of the game.

        Arguments:
            Source and destination: automatically specified choices.
        """
        self.change_disks_location_from_one_rod_to_another(source, destination)
        time.sleep(self.wait_time)
        self.gui_funcs["show_state"]()

    def auto_solve_algorithm(
            self, n_disks: int, source: str, destination: str, placeholder: str
    ) -> None:
        """Algorithm solving the game and displaying each step to the GUI."""
        if n_disks == 1:
            self.make_and_show_1_move(source, destination)
            return None
        self.auto_solve_algorithm(n_disks - 1, source, placeholder, destination)
        self.make_and_show_1_move(source, destination)
        self.auto_solve_algorithm(n_disks - 1, placeholder, destination, source)
        self.gui_funcs["show_state"]()

    def play_again_if_player_wants_to(self):
        """Asks the player if he/she wants to play again and
        restarts the game if so.
        """
        play_again = self.gui_funcs['play_again']()
        if play_again:
            self.gui_funcs['restart']()

    def start_game(self) -> None:
        """Starts the game and runs it until winning conditions are satisfied."""
        solver = self.gui_funcs['get_solver']()

        if solver == 'y':
            while not self.check_if_right_rod_full_and_others_empty():  # Winning condition
                self.gui_funcs['show_state']()
                self.make_move()
            self.gui_funcs['game_won']()
            self.play_again_if_player_wants_to()

        elif solver == 'a':
            while not self.check_if_right_rod_full_and_others_empty():  # Winning condition
                self.auto_solve_algorithm(self.number_of_disks, 'left', 'right', 'central')
            self.play_again_if_player_wants_to()
