import unittest
from unittest import mock

from tower_of_hanoi.game_backend import Game


class TestGameInitialization(unittest.TestCase):
    def setUp(self):
        gui_func_dict = {'difficulty': 5}
        self.game = Game(gui_func_dict)

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


class TestGameInitialized(unittest.TestCase):
    def setUp(self):
        gui_func_dict = {'difficulty': 5}
        self.game = Game(gui_func_dict)

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
            mock_disk_from_source.\
                check_if_target_disk_below_exists_and_is_bigger.\
                assert_called_with(None)

            self.game.check_if_player_destination_choice_correct(
                'left', mock_disk_from_source)
            left_top_disk = self.game.rod1.peek_element_from_top()
            mock_disk_from_source.\
                check_if_target_disk_below_exists_and_is_bigger.\
                assert_called_with(left_top_disk)

    def test_get_source_rod_with_correct_input(self):
        # This won't work with central and right, as these rods are empty.
        input_list = ['l', 'left']
        with mock.patch('builtins.input') as mock_input:
            for player_input in input_list:
                mock_input.return_value = player_input
                self.assertTrue('left', self.game.get_source_rod())

    def test_fet_source_rod_prints_result(self):
        # This won't work with central and right, as these rods are empty.
        with mock.patch('builtins.input') as mock_input:
            with mock.patch('builtins.print') as mock_print:
                mock_input.return_value = 'l'
                self.assertTrue('left', self.game.get_source_rod())
                mock_print.assert_called_with('Source: ', 'left')

    def test_get_destination_rod_with_correct_input(self):
        input_list = ['l', 'left', 'r', 'right', 'c', 'central']

        with mock.patch('builtins.input') as mock_input:
            with mock.patch('tower_of_hanoi.disk.Disk') as mock_disk_from_source:
                for player_input in input_list:
                    mock_input.return_value = player_input

                    self.assertTrue(
                        input_list,
                        self.game.get_destination_rod(mock_disk_from_source))

                    mock_disk_from_source.\
                        check_if_target_disk_below_exists_and_is_bigger.\
                        assert_called()

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
        self.assertEqual(2, self.game.rod1.peek_element_from_top().size)
        self.assertEqual(1, self.game.rod3.peek_element_from_top().size)
        self.assertEqual(4, self.game.rod1.get_size())

    def test_check_if_right_rod_full_and_others_empty(self):
        gui_func_dict = {'difficulty': 2}
        game = Game(gui_func_dict)
        self.assertFalse(game.check_if_right_rod_full_and_others_empty())

        # Winning moves for difficulty level 2
        game.change_disks_location_from_one_rod_to_another('left', 'central')
        game.change_disks_location_from_one_rod_to_another('left', 'right')
        game.change_disks_location_from_one_rod_to_another('central', 'right')
        self.assertTrue(game.check_if_right_rod_full_and_others_empty())


if __name__ == '__main__':
    unittest.main()
