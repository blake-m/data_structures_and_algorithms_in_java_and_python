""""""
from tower_of_hanoi.game import Game


class TextGUI:
    def __init__(self):
        gui_functions_dictionary: dict = {
            "difficulty": self.ask_player_difficulty_level()
        }
        self.game = Game(gui_functions_dictionary)

    def ask_player_difficulty_level(self) -> int:
        # Prompt player for it and convert to int
        return 5


    def print_current_state(self):
        print('\n' * 25)
        for rod in self.game.rods_dictionary.values():
            if rod.is_empty():
                print(rod.name, ": Empty")
            else:
                disks_representations = [disk.size * '@' for disk in iter(rod)]
                print(rod.name, ": ", disks_representations)