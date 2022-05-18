import unittest
from unittest.mock import patch
from toy_car.car import Car


@patch("toy_car.table.Table")
class TestingFunction(unittest.TestCase):

    def test_car_report(self, mock_table):

        car = Car(mock_table)

        self.assertRaises(ValueError, car.report)


if __name__ == '__main__':
    unittest.main()
