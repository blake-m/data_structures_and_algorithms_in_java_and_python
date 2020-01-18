import unittest

from tower_of_hanoi.game import Game


class TestGameInitialization(unittest.TestCase):
    # TODO: use mock/stub to test this one
    def test_initialization_rods_dictionary_contains_3_rod_members(self):
        game = Game()


class TestGameInitialized(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
