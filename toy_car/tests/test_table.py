import unittest
from toy_car.table import Table


class TestingTable(unittest.TestCase):

    def setUp(self) -> None:

        # We assume that table is always 5x5
        self.table = Table()

    def test_check_validate_position(self):

        # This has to be False
        self.assertFalse(self.table.check_position(-1, -1))
        self.assertFalse(self.table.check_position(-2, -2))
        self.assertFalse(self.table.check_position(5, -1))
        self.assertFalse(self.table.check_position(1, -1000))

        # This has to be True
        self.assertTrue(self.table.check_position(4, 4))
        self.assertTrue(self.table.check_position(3, 3))
        self.assertTrue(self.table.check_position(0, 4))
        self.assertTrue(self.table.check_position(3, 1))

