from toy_car.car import Car
from toy_car.table import Table

"""
    This is a 5x5 table top, 
        - 0 = No car
        - 1 = Has car
"""


def run_car(valid_commands):

    # Allocate a car to a table, but the car has not been placed yet.
    table = Table()
    car = Car(table)

    # The commands come in format for a list with format [(string, int, int, string), string string, string]
    # The commands are trusted as they have been validated in the command processor, therefore we don't do checks here.
    for index, item in enumerate(valid_commands):

        # if it is a tuple, we expect a place
        if type(item) is tuple:

            car.place(item[1], item[2], item[3])

        else:

            command = item

            if command == "REPORT":

                car.report()

            elif command == "MOVE":

                car.move()

            elif command == "LEFT":

                car.rotate('LEFT')

            elif command == "RIGHT":

                car.rotate("RIGHT")