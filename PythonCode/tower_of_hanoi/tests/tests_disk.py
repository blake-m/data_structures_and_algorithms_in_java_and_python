import unittest

from tower_of_hanoi.disk import Disk


class TestDisk(unittest.TestCase):
    def setUp(self):
        self.small_disk = Disk(1)
        self.big_disk = Disk(12)

    def test_size(self):
        self.assertEqual(self.small_disk.size, 1)
        self.assertEqual(self.big_disk.size, 12)

    def test_check_if_there_is_disk_below_returns_true_with_no_disk(self):
        self.assertTrue(self.small_disk.check_if_target_disk_below_exists_and_is_bigger(None))

    def test_check_if_there_is_disk_below_returns_true_with_bigger_disk(self):
        self.assertTrue(self.small_disk.check_if_target_disk_below_exists_and_is_bigger(self.big_disk))

    def test_check_if_there_is_disk_below_returns_false_with_smaller_disk(self):
        self.assertFalse(self.big_disk.check_if_target_disk_below_exists_and_is_bigger(self.small_disk))


if __name__ == "__main__":
    unittest.main()
