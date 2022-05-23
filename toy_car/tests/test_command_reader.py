import unittest
from toy_car.command_reader import read_commands, convert_and_validate_first_command
from unittest.mock import patch
import os

TEST_BAD_DATA_FILENAME = os.path.join(os.path.dirname(__file__), 'test_data/very_bad_data.txt')
TEST_GOOD_DATA_FILENAME = os.path.join(os.path.dirname(__file__), 'test_data/good_data.txt')
TEST_EMPTY_DATA_FILENAME = os.path.join(os.path.dirname(__file__), 'test_data/empty_data.txt')


class TestingCommandFunction(unittest.TestCase):

    # The read commands should not invoke validate_and_clean_commands() if the file has no PLACE
    @patch('toy_car.command_reader.validate_and_clean_commands')
    def test_command_file_reader_not_called_validate(self, mock):

        read_commands(TEST_BAD_DATA_FILENAME)
        mock.assert_not_called()

    # The read commands should invoke validate_and_clean_commands() if the file has PLACE
    @patch('toy_car.command_reader.validate_and_clean_commands')
    def test_command_file_reader_call_validate(self, mock):

        read_commands(TEST_GOOD_DATA_FILENAME)
        mock.assert_called()

    # If there is an error in converting the PLACE command, it should raise error
    def test_convert_and_validate_first_command(self):

        self.assertRaises(ValueError, convert_and_validate_first_command, 'PLACE', 0, 1, "NARTH")
        self.assertRaises(ValueError, convert_and_validate_first_command, 'PLAZE', 0, 1, "SOOTH")

    # If the file is empty, the program should not construct a car object.
    @patch('toy_car.runner.run_car')
    def test_run_car(self, mock):

        read_commands(TEST_EMPTY_DATA_FILENAME)
        mock.assert_not_called()






