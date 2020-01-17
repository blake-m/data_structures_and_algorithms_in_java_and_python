import unittest

from tower_of_hanoi.disk import Disk


class TestDisk(unittest.TestCase):
    def setUp(self):
        self.small_disk = Disk(1)
        self.big_disk = Disk(12)

    def test_size(self):
        self.assertEqual(self.small_disk.size, 1)
        self.assertEqual(self.big_disk.size, 12)

    def test_check_if_there_is_disk_below(self):
        self.assertTrue(self.small_disk.check_if_there_is_disk_below(self.big_disk))

    def test_check_if_there_is_disk_below_fails_with_none_argument(self):
        self.assertFalse(self.small_disk.check_if_there_is_disk_below(None))

    def test_check_if_disk_below_is_bigger_fails_with_smaller_disk_below(self):
        self.assertFalse(self.big_disk.check_if_disk_below_is_bigger(self.small_disk))

    def test_check_if_disk_can_be_moved_onto_specified_rod(self):
        self.assertTrue(
            self.small_disk.check_if_disk_can_be_moved_onto_specified_rod(self.big_disk)
        )


if __name__ == "__main__":
    unittest.main()
