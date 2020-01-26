import unittest
from unittest import mock

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

    def test_push_disk_on_top_calls_disks_checks_1_element(self):
        with mock.patch('tower_of_hanoi.disk.Disk') as disk_mock:
            self.rod1.push_disk_on_top(disk_mock)
            current_top_disk = None     # now rod1 is empty

            disk_mock.check_if_disk_below_exists_and_is_bigger\
                .assert_called_with(current_top_disk)

    def test_push_disk_on_top_calls_disks_checks_2_elements(self):
        with mock.patch('tower_of_hanoi.disk.Disk') as disk_mock:
            self.rod1.push_disk_on_top(disk_mock)  # now rod1 is empty
            self.rod1.push_disk_on_top(disk_mock)  # now rod1 has a disk already

            current_top_disk = self.rod1.peek_element_from_top()
            disk_mock.check_if_disk_below_exists_and_is_bigger\
                .assert_called_with(current_top_disk)

    def test_push_disk_on_top_increases_rod_stack_size(self):
        with mock.patch('tower_of_hanoi.disk.Disk') as disk_mock:
            self.rod1.push_disk_on_top(disk_mock)  # now rod1 is empty
            self.assertEqual(1, self.rod1.get_size())

    def test_push_disk_on_top_check_top_element(self):
        with mock.patch('tower_of_hanoi.disk.Disk') as disk_mock:
            self.rod1.push_disk_on_top(disk_mock)  # now rod1 is empty
            self.assertEqual(disk_mock, self.rod1.peek_element_from_top())


if __name__ == "__main__":
    unittest.main()
