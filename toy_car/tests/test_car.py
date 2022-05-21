import unittest
from toy_car.car import Car
from toy_car.table import Table


class TestingCarFunction(unittest.TestCase):

    def setUp(self) -> None:

        self.table = Table()

    # report() Should raise ValueError before placed
    def test_car_report_before_place(self):

        car = Car(self.table)

        self.assertRaises(ValueError, car.report)

    # move() should run without exception if the position is valid
    def test_car_move_before_place(self):

        car = Car(self.table)

        self.assertRaises(ValueError, car.move)

    # move() should run after a car has been placed placed
    def test_car_move_after_place(self):

        car = Car(self.table)
        car.place(0, 0, "NORTH")
        self.assertEqual(car.move(), True)

    def test_over_placed(self):

        car = Car(self.table)

        self.assertRaises(IndexError, car.place, 6, 6, "SOUTH")
        self.assertRaises(IndexError, car.place, 7, 8, "SOUTH")
        self.assertRaises(IndexError, car.place, -1, 3, "WEST")
        self.assertRaises(IndexError, car.place, 100, 1000, "NORTH")
        self.assertRaises(IndexError, car.place, 5, 0, "NORTH")

    # a car should not when it can't
    def test_move_invalid_position(self):

        car = Car(self.table)
        car.place(0, 0, "SOUTH")
        self.assertEqual(car.move(), False)
        car.place(4, 4, "EAST")
        self.assertEqual(car.move(), False)
        car.place(4, 0, "EAST")
        self.assertEqual(car.move(), False)
        car.place(4, 2, "EAST")
        self.assertEqual(car.move(), False)
        car.place(0, 4, "WEST")
        self.assertEqual(car.move(), False)
        car.place(0, 2, "WEST")
        self.assertEqual(car.move(), False)


if __name__ == '__main__':
    unittest.main()
