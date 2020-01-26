""""""
from typing import Any, Dict

from tower_of_hanoi.game_backend import Game


class TextGUI:
    def __init__(self) -> None:
        gui_func_dict: Dict[str, Any] = self.create_gui_func_dict()
        self.game: Game = Game(gui_func_dict)
        self.game.start_game()

    def create_gui_func_dict(self) -> Dict[str, Any]:  # TODO(blake) fix type annotations at the end
        gui_func_dict = {
            "difficulty": self.ask_player_difficulty_level,
            "get_solver": self.ask_player_who_solves,
            "show_state": self.show_current_state,
            "get_wait_time": self.ask_player_wait_time_each_algorithm_step,
            "source_choose_again": self.ask_player_choose_source_rod_again,
            "destination_choose_again": self.ask_player_choose_destination_rod_again,
            "game_won": self.show_congratulations,
            "play_again": self.ask_player_play_again,
            "restart": self.restart_game,
        }
        return gui_func_dict

    def ask_player_difficulty_level(self) -> int:
        # Prompt player for it and convert to int
        return 12

    def ask_player_wait_time_each_algorithm_step(self):
        return 0

    @staticmethod
    def ask_player_choose_source_rod_again():
        print("You can't take disks from an EMPTY rod. Choose again.")

    @staticmethod
    def ask_player_choose_destination_rod_again():
        print("You are either trying to:"
              "\n\t- put a BIGGER DISK onto a SMALLER DISK. "
              "\n\t- choose the same rod twice. "
              "\nThese can't be done. Choose again.")

    @staticmethod
    def show_congratulations():
        print('Congrats')

    @staticmethod
    def ask_player_who_solves():
        return input('Want to solve it yourself [y]? '
                     '\nOr see the auto algorithm solution [a]?\n')

    @staticmethod
    def ask_player_play_again() -> bool:
        answer = input('Do you want to play again? [y] for Yes, [n] for No.')
        if answer == 'y':
            return True
        elif answer == 'n':
            print("Goodbye!")
            return False
        print("Invalid Choice. Let's try one more time")
        TextGUI.ask_player_play_again()

    def show_current_state(self):
        print('\n' * 25)
        for rod in self.game.rods_dictionary.values():
            if rod.is_empty():
                print(rod.name, ": Empty")
            else:
                disks_representations = self.form_disks_representation(rod)
                print(rod.name, ": ", disks_representations)

    @staticmethod
    def form_disks_representation(rod):
        return [disk.size * '@' for disk in iter(rod)]

    def restart_game(self):
        print('\n'*25)
        self.__init__()
