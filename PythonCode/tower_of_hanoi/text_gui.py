"""Text Graphical User Interface for Tower of Hanoi (ToH)."""
from typing import Any, Dict, Callable, List

from tower_of_hanoi.game_backend import Game


class TextGUI:
    """Imports and initializes ToH backend mechanics and provides GUI for it."""
    def __init__(self) -> None:
        """Initializes Tower of Hanoi game and passes all GUI functions in
        a form of dictionary to it. Thanks to that GUI is controlled by game
        mechanics."""
        gui_func_dict: Dict[str, Any] = self.create_gui_func_dict()
        self.game: Game = Game(gui_func_dict)
        self.game.start_game()

    def create_gui_func_dict(self) -> Dict[str, Callable]:
        gui_func_dict = {
            "difficulty": self.ask_player_difficulty_level,
            "get_solver": self.ask_player_who_solves,
            "show_state": self.show_current_state,
            "get_wait_time": self.ask_player_wait_time_each_algorithm_step,
            "show_source_choice": self.show_source_choice,
            "show_destination_choice": self.show_destination_choice,
            "source_choose_again": self.ask_player_choose_source_rod_again,
            "destination_choose_again": self.ask_player_choose_destination_rod_again,
            "game_won": self.show_congratulations,
            "play_again": self.ask_player_play_again,
            "restart": self.restart_game,
        }
        return gui_func_dict

    def ask_player_difficulty_level(self) -> int:
        """Asks player to specify difficulty level.

        If the answer provided by the player is not a correct value or a value
        not within the range accepted by the game, recursively restarts the
        function."""
        try:
            choice = int(input(
                "Choose difficulty level (the number of disks to move)."
                "\n\t <choose a number between 1 and 12>"
            ))
            if choice >= 1 & choice <= 12:
                return choice
            raise ValueError
        except ValueError:
            print('\n' * 25,
                  'Incorrect choice. It has to be a number between 1 and 12.'
                  '\nTry again.\n')
            self.ask_player_difficulty_level()

    def ask_player_wait_time_each_algorithm_step(self) -> int:
        """Asks player to specify time that algorithm waits after each move.

        If the answer provided by the player is not a correct value or a value
        not within the range accepted by the game, recursively restarts the
        function."""
        try:
            choice = int(input(
                "How long do you want to wait after each "
                "algorithm's step to observe the solution process?"
                "\n\t <choose a number between 1 and 6>"
            ))
            if choice >= 1 & choice <= 6:
                return choice
            raise ValueError
        except ValueError:
            print('\n' * 25,
                  'Incorrect choice. It has to be a number between 1 and 6.'
                  '\nTry again.\n')
            self.ask_player_wait_time_each_algorithm_step()

    @staticmethod
    def ask_player_choose_source_rod_again():
        """Displays a message to a player."""
        print("You can't take disks from an EMPTY rod. Choose again.")

    @staticmethod
    def ask_player_choose_destination_rod_again():
        """Displays a message to a player."""
        print("You are either trying to:"
              "\n\t- put a BIGGER DISK onto a SMALLER DISK. "
              "\n\t- choose the SAME ROD twice. "
              "\n\t- not give a proper DISK NAME. "
              "\nThese can't be done. Choose again.")

    @staticmethod
    def show_congratulations() -> None:
        """Displays a message to a player."""
        print('Congratulations, you won!\n')

    def ask_player_who_solves(self) -> str:
        """Asks player whether they want to solve the game on their own or
        see the solution of the self-solving algorithm.

        If the answer provided by the player is not a correct value or a value
        not within the range accepted by the game, recursively restarts the
        function."""
        correct_choices = ['y', 'a']
        choice = input('Want to solve it yourself [y]? '
                       '\nOr see the auto-solving algorithm solution [a]?\n')
        if choice not in correct_choices:
            print('\n'*25,
                  'Incorrect choice. It has to be either'
                  '\n\tyou [y] \n\tor the algorithm [a]. \nTry again.\n')
            self.ask_player_who_solves()
        return choice

    @staticmethod
    def ask_player_play_again() -> bool:
        """Asks player whether they want to play again.

        If the answer provided by the player is not a correct value or a value
        not within the range accepted by the game, recursively restarts the
        function."""
        answer = input('Do you want to play again? [y] for Yes, [n] for No.')
        if answer == 'y':
            return True
        elif answer == 'n':
            print("Goodbye!")
            return False
        print("Invalid Choice. Let's try one more time")
        TextGUI.ask_player_play_again()

    @staticmethod
    def show_source_choice(player_source_choice: str) -> None:
        """Shows the current choice of source rod made by player."""
        print('Source:', player_source_choice)

    @staticmethod
    def show_destination_choice(player_destination_choice: str) -> None:
        """Shows the current choice of destination rod made by player."""
        print('Destination:', player_destination_choice)

    def show_current_state(self) -> None:
        """Shows the current state of the game.

        Disks are represented by sets of @. Their size is represented by
        the number of @ signs in the set. If the rod doesn't have any disks
        on it right now, 'Empty' message is displayed. Example of correctly
        printed game state.

        left :  ['@@@@@', '@@@@', '@']
        central :  ['@@']
        right :  ['@@@']
        """
        print('\n' * 25)
        for rod in self.game.rods_dictionary.values():
            if rod.is_empty():
                print(rod.name, ": Empty")
            else:
                disks_representations = self.form_disks_representation(rod)
                print(rod.name, ": ", disks_representations)

    @staticmethod
    def form_disks_representation(rod) -> List[str]:
        """Creates a text representation for each disk.

        Disks are represented by sets of @. Their size is represented by
        the number of @ signs in the set."""
        return [disk.size * '@' for disk in iter(rod)]

    def restart_game(self) -> None:
        """Restarts the game and clears the screen."""
        print('\n'*25)
        self.__init__()
