import unittest

from tower_of_hanoi.disk import Disk
from tower_of_hanoi.rod import Rod


class TestRod(unittest.TestCase):
    def setUp(self):
        self.rod1 = Rod('Left')

    def test_initialization_adds_members_to_members_dictionary(self):
        self.rod2 = Rod('Central')
        self.rod3 = Rod('Right')
        self.assertEqual(Rod.members_dictionary['Left'], self.rod1)
        self.assertEqual(Rod.members_dictionary['Central'], self.rod2)
        self.assertEqual(Rod.members_dictionary['Right'], self.rod3)

    def test_name_returns_string_with_name(self):
        self.assertEqual(self.rod1.name, 'Left')

    def test_push_disk_on_top(self):
        # TODO: use mock/stub to test this one
        pass


if __name__ == "__main__":
    unittest.main()
