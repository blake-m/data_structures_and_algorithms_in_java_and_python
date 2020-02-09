import copy
import unittest
from unittest import mock

from tower_of_hanoi.game_backend import Game

# Mocks reused in setUps - gdf = gui_dict_func
_gdf_difficulty_mock = mock.Mock(return_value=5)
_gdf_get_solver_mock = mock.Mock(return_value='a')
_gdf_show_state_mock = mock.Mock()
_gdf_get_wait_time_mock = mock.Mock(return_value=1)
_gdf_show_source_choice = mock.Mock()
_gdf_show_destination_choice = mock.Mock()
_gdf_source_choose_again_mock = mock.Mock()
_gdf_destination_choose_again_mock = mock.Mock()
_gdf_game_won_mock = mock.Mock()
_gdf_play_again_mock = mock.Mock(return_value=True)
_gdf_restart_mock = mock.Mock()

_gui_func_dict = {
    'difficulty': _gdf_difficulty_mock,
    "get_solver": _gdf_get_solver_mock,
    "show_state": _gdf_show_state_mock,
    'get_wait_time': _gdf_get_wait_time_mock,
    "show_source_choice": _gdf_show_source_choice,
    "show_destination_choice": _gdf_show_destination_choice,
    "source_choose_again": _gdf_source_choose_again_mock,
    "destination_choose_again": _gdf_destination_choose_again_mock,
    "game_won": _gdf_game_won_mock,
    "play_again": _gdf_play_again_mock,
    "restart": _gdf_restart_mock,
}


class TestGameInitialization(unittest.TestCase):
    def setUp(self):
        self.game = Game(_gui_func_dict)

    def test_initialization_rods_dictionary_contains_3_rod_members(self):
        self.assertEqual(3, len(self.game.rods_dictionary))

    def test_initialization_rods_dictionary_check_names(self):
        self.assertEqual('left', self.game.rods_dictionary['left'].name)
        self.assertEqual('central', self.game.rods_dictionary['central'].name)
        self.assertEqual('right', self.game.rods_dictionary['right'].name)

    def test_initialization_left_rod_contains_3_disks(self):
        self.assertEqual(5, self.game.rods_dictionary['left'].get_size())

    def test_initialization_central_rod_contains_0_disks(self):
        self.assertEqual(0, self.game.rods_dictionary['central'].get_size())

    def test_initialization_right_rod_contains_0_disks(self):
        self.assertEqual(0, self.game.rods_dictionary['right'].get_size())

    def test_initialization_difficulty_time_was_called(self):
        _gdf_difficulty_mock.assert_called()

    def test_initialization_get_wait_time_was_called(self):
        _gdf_get_wait_time_mock.assert_called()


class TestGameInitialized(unittest.TestCase):
    def setUp(self):
        self.game = Game(_gui_func_dict)

    def test_get_full_choice_string_from_1_letter_choice_correct_choices(self):
        correct_choices_list = ['l', 'r', 'c', 'left', 'right', 'central']
        converted_correct_choices = ['left', 'right', 'central']
        for choice in correct_choices_list:
            converted_choice = \
                self.game.get_full_choice_string_from_1_letter_choice(choice)
            self.assertIn(converted_choice, converted_correct_choices)

    def test_get_full_choice_string_from_1_letter_choice_wrong_choices(self):
        correct_choices_list = ['s', 'q', 'a', 'Le', 'last', 'centrum']
        converted_correct_choices = ['left', 'right', 'central']
        for choice in correct_choices_list:
            converted_choice = \
                self.game.get_full_choice_string_from_1_letter_choice(choice)
            self.assertNotIn(converted_choice, converted_correct_choices)

    def test_get_full_choice_string_from_1_letter_choice_throws_error_with_none(self):
        with self.assertRaises(AttributeError):
            self.game.get_full_choice_string_from_1_letter_choice(None)

    def test_check_if_choice_in_available_choices(self):
        for choice in ['left', 'right', 'central']:
            self.assertTrue(self.game.check_if_choice_in_available_choices(choice))
        for choice in ['Lefft', 'centrum', 'rajt']:
            self.assertFalse(self.game.check_if_choice_in_available_choices(choice))

    def test_check_if_player_source_choice_correct(self):
        self.assertTrue(self.game.check_if_player_source_choice_correct('left'))
        self.assertFalse(self.game.check_if_player_source_choice_correct('central'))
        self.assertFalse(self.game.check_if_player_source_choice_correct('right'))

    def test_check_if_player_destination_choice_correct(self):
        with mock.patch('tower_of_hanoi.disk.Disk') as mock_disk_from_source:
            self.game.check_if_player_destination_choice_correct(
                'right', mock_disk_from_source)
            mock_disk_from_source. \
                check_if_target_disk_below_exists_and_is_bigger. \
                assert_called_with(None)

            self.game.check_if_player_destination_choice_correct(
                'left', mock_disk_from_source)
            left_top_disk = self.game.rod1.peek_element_from_top()
            mock_disk_from_source. \
                check_if_target_disk_below_exists_and_is_bigger. \
                assert_called_with(left_top_disk)

    def test_get_source_rod_with_correct_input(self):
        # This won't work with central and right, as these rods are empty.
        input_list = ['l', 'left']
        with mock.patch('builtins.input') as mock_input:
            for player_input in input_list:
                mock_input.return_value = player_input
                self.assertTrue('left', self.game.get_source_rod())

    def test_get_source_rod_calls_proper_gui_method(self):
        with mock.patch('builtins.input') as mock_input:
            mock_input.return_value = 'left'
            self.game.get_source_rod()
            _gdf_show_source_choice.assert_called_with('left')

    def test_get_destination_rod_with_correct_input(self):
        input_list = ['l', 'left', 'r', 'right', 'c', 'central']

        with mock.patch('builtins.input') as mock_input:
            with mock.patch('tower_of_hanoi.disk.Disk') as mock_disk_from_source:
                for player_input in input_list:
                    mock_input.return_value = player_input

                    self.assertTrue(
                        input_list,
                        self.game.get_destination_rod(mock_disk_from_source))

                    mock_disk_from_source. \
                        check_if_target_disk_below_exists_and_is_bigger. \
                        assert_called()

    def test_get_destination_rod_calls_proper_gui_method(self):
        with mock.patch('builtins.input') as mock_input:
            with mock.patch('tower_of_hanoi.disk.Disk') as mock_disk:
                mock_input.return_value = 'right'
                self.game.get_destination_rod(mock_disk)
                _gdf_show_destination_choice.assert_called_with('right')

    def test_ask_player_for_destination_and_source_rods(self):
        # Due to infinite loops this function can't be tested.
        pass

    def test_change_disks_location_from_one_rod_to_another_moves_element(self):
        # I provide only correct strings as their validity is
        # thoroughly tested by other functions.
        disk_moved = self.game.rod1.peek_element_from_top()
        self.game.change_disks_location_from_one_rod_to_another('left', 'right')
        self.assertEqual(disk_moved, self.game.rod3.peek_element_from_top())

    def test_change_disks_location_from_one_rod_to_another_removes_element(self):
        # I provide only correct strings as their validity is
        # thoroughly tested by other functions.
        disk_moved = self.game.rod1.peek_element_from_top()
        self.game.change_disks_location_from_one_rod_to_another('left', 'right')
        print(self.game.rod1.get_size())
        print(self.game.rod2.get_size())
        print(self.game.rod3.get_size())
        self.assertEqual(2, self.game.rod1.peek_element_from_top().size)
        self.assertEqual(1, self.game.rod3.peek_element_from_top().size)
        self.assertEqual(4, self.game.rod1.get_size())

    def test_check_if_right_rod_full_and_others_empty(self):
        _gdf_get_difficulty_mock_return_2 = mock.Mock(return_value=2)
        gui_func_dict = {
            'difficulty': _gdf_get_difficulty_mock_return_2,
            'get_wait_time': _gdf_get_wait_time_mock,
        }
        game = Game(gui_func_dict)
        self.assertFalse(game.check_if_right_rod_full_and_others_empty())

        # Winning moves for difficulty level 2
        game.change_disks_location_from_one_rod_to_another('left', 'central')
        game.change_disks_location_from_one_rod_to_another('left', 'right')
        game.change_disks_location_from_one_rod_to_another('central', 'right')
        self.assertTrue(game.check_if_right_rod_full_and_others_empty())

    def test_make_move_moves_the_disk(self):
        func_path = "tower_of_hanoi.game_backend.Game." \
                    "ask_player_for_destination_and_source_rods"
        with mock.patch(func_path)\
                as ask_player_for_destination_and_source_rods:
            ask_player_for_destination_and_source_rods.return_value = 'left', 'right'
            self.game.make_move()
            self.assertEqual(1, self.game.rod3.peek_element_from_top().size)

    def test_make_move_calls_proper_methods(self):
        game_class = "tower_of_hanoi.game_backend.Game"
        func_1_name = "ask_player_for_destination_and_source_rods"
        func_2_name = "change_disks_location_from_one_rod_to_another"

        with mock.patch(f'{game_class}.{func_1_name}') \
                as ask_player_for_destination_and_source_rods,\
                mock.patch(f'{game_class}.{func_2_name}')\
                as change_disks_location_from_one_rod_to_another:
            ask_player_for_destination_and_source_rods.return_value = 'l', 'r'
            self.game.make_move()
            ask_player_for_destination_and_source_rods.assert_called()
            change_disks_location_from_one_rod_to_another.assert_called_with(
                'l', 'r')

    def test_make_and_show_1_move_moves_disks(self):
        """This is tested only with correct inputs as the algorithm cannot
        make mistakes in its moves."""
        self.game.make_and_show_1_move('left', 'right')
        self.assertEqual(1, self.game.rod3.peek_element_from_top().size)

    def test_make_and_show_1_move_prints_calls_proper_methods(self):
        """This is tested only with correct inputs as the algorithm cannot
        make mistakes in its moves."""
        with mock.patch('time.sleep') as sleep_mock:
            self.game.make_and_show_1_move('left', 'right')
            sleep_mock.assert_called_with(1)
            _gdf_show_state_mock.assert_called()

    def test_play_again_if_player_wants_to_player_says_yes(self):
        _gdf_play_again_mock.return_value = True
        self.game.play_again_if_player_wants_to()
        _gdf_play_again_mock.assert_called()
        _gdf_restart_mock.assert_called()

    def test_play_again_if_player_wants_to_player_says_no(self):
        _gdf_play_again_mock.return_value = False
        self.game.play_again_if_player_wants_to()
        _gdf_play_again_mock.assert_called()
        _gdf_restart_mock.assert_not_called()

    def test_auto_solve_algorithm_calls_proper_methods(self):
        # Time is mocked to not wait for every move
        with mock.patch('time.sleep') as sleep_mock:
            for difficulty in range(1, 13):
                _gdf_difficulty_mock.return_value = difficulty
                game = Game(_gui_func_dict)
                self.game.auto_solve_algorithm(difficulty, 'left', 'right', 'central')
                _gdf_difficulty_mock.assert_called()
                _gdf_get_wait_time_mock.assert_called()
                _gdf_show_state_mock.assert_called()

    def test_auto_solve_algorithm_solves_the_game(self):
        # Time is mocked not to wait for every move
        with mock.patch('time.sleep') as sleep_mock:
            for difficulty in range(1, 13):
                _gdf_difficulty_mock_separated = mock.Mock(return_value=difficulty)
                _gui_func_dict_separated = copy.deepcopy(_gui_func_dict)
                _gui_func_dict_separated['difficulty'] = _gdf_difficulty_mock_separated
                _gdf_difficulty_mock.return_value = difficulty
                game = Game(_gui_func_dict_separated)
                self.assertEqual(difficulty, game.rod1.get_size())
                self.game.auto_solve_algorithm(difficulty, 'left', 'right', 'central')
                self.assertEqual(0, game.rod1.get_size())
                self.assertEqual(0, game.rod2.get_size())
                self.assertEqual(difficulty, game.rod3.get_size())


if __name__ == '__main__':
    unittest.main()
