import argparse
from toy_car.runner import run_car
from toy_car.root_logger import logger
from toy_car.settings import LIST_OF_CAR_COMMANDS


def convert_and_validate_first_command(c1, c2, c3, c4):

    """
    There are couple rules that need to be followed
    1st index is a string PLACE
    2nd index is a positive integer
    3rd index is a string NORTH SOUTH EAST WEST
    """

    r1 = c1
    r2 = c2
    r3 = c3
    r4 = c4
    errors = []

    try:
        r2 = int(c2)
        r3 = int(c3)
    except ValueError:
        errors.append("x and y values are not integer.")
    if r4 not in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
        errors.append('Direction has to be NORTH SOUTH EAST WEST.')
    # Perform another check in case convert_and_validate_first_command is not used appropriately
    if r1 != "PLACE":
        errors.append('Argument c1 is not PLACE')
    if len(errors) > 0:
        raise ValueError(
            'Your first command is PLACE but the following command values are incorrect. Here are the problems - {0}'.format(
                ' '.join(errors)))
    else:
        return r1, r2, r3, r4


def validate_and_clean_commands(command):

    """
    Validate lines from the txt file, commands that are not in the list are discarded.
    If PLACE parameters are incorrect, raise errors.
    """

    # This will discard a command until valid PLACE has been put.
    if command.startswith("PLACE"):

        # Place has format of PLACE x,y,direction
        split_place = command.split(" ")

        if len(split_place) == 2:

            split_val = split_place[1].split(',')

            if len(split_val) == 3:

                return convert_and_validate_first_command("PLACE", split_val[0], split_val[1], split_val[2])

        else:

            raise ValueError("Incorrect parameter in PLACE")

    else:

        return command


def read_commands(file_name):

    file = open(file_name, 'r')
    lines = file.readlines()

    valid_commands = []

    place_found = False

    for i, line in enumerate(lines):

        strip_line = line.strip()

        # skips all the line until place is found

        if strip_line.startswith("PLACE"):

            logger.debug('Found a PLACE command at line {0}'.format(i + 1))

            place_found = True

        # if place has been found, proceed to run validation, else keep skipping
        if place_found:

            if strip_line != "":

                is_command = line.startswith(LIST_OF_CAR_COMMANDS)

                if is_command:

                    command = validate_and_clean_commands(strip_line)

                    valid_commands.append(command)
                else:
                    logger.debug("Removing {0} command as it is not supported".format(line))

    file.close()

    if len(valid_commands) > 0:

        logger.debug(valid_commands)

        run_car(valid_commands)

    else:

        logger.warning("No valid commands found in {0}".format(file_name))


def main():

    """
    Read commands from .txt file
    """

    parser = argparse.ArgumentParser(prog="drive")
    parser.add_argument('file', help='The input file for the robot. This file need to be placed on the root directory')
    parser.add_argument('--verbose', nargs='?', const='arg_was_not_given', help='Print out debug logs')

    args = parser.parse_args()

    if args.verbose is not None:
        logger.setLevel("DEBUG")
    else:
        logger.setLevel("INFO")

    read_commands(args.file)