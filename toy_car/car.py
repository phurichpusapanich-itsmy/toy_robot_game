from toy_car.utilities import check_has_placed
from toy_car.settings import DIRECTION, DIRECTION_MOVE_VALUES, INVERSE_DIRECTION
from toy_car.table import Table
from toy_car.root_logger import logger


class Car:
    """
    Base class for Car that can move in 2D grid.

    A car is given a 2D grid to drive on

    Function:
        place - params: x, y, facing
        rotate - params: which(LEFT, RIGHT)
        move - params:
        compute_command - params: command

    The settings are declared in settings.py, you will not able to drive a car without settings

    """

    def __init__(self, table: Table):
        self.has_placed = False
        self.x = None
        self.y = None
        self.facing = None
        self.table = table

    def place(self, x: int, y: int, facing: str):

        # This is is an input, we need to enforce int here
        if not isinstance(x, int):
            raise TypeError("bar must be set to an integer")
        if not isinstance(y, int):
            raise TypeError("bar must be set to an integer")

        if not self.table.check_position(x, y):
            raise IndexError("A car cannot be placed on that posit6ion")

        self.has_placed = True
        self.x = x
        self.y = y

        # When placing facing/direction, check if those are keys in the direction dict declared above
        if facing in DIRECTION:
            self.facing = facing
        else:
            raise ValueError("A car cannot be placed on that position")

    @check_has_placed
    def report(self):

        logger.info("The car is at {0}, {1} and is facing {2}".format(self.x, self.y, self.facing))

    @check_has_placed
    def move(self):

        # Move +1 if NORTH MOVE -1 If SOUTH

        move_val = DIRECTION_MOVE_VALUES[self.facing]
        if self.facing == "NORTH" or self.facing == "SOUTH":
            can_move = self.table.check_position(self.x, self.y + move_val)
            if can_move:
                self.y = self.y + move_val
                logger.debug("Moving to {0} {1}".format(self.x, self.y))
                return True
            else:
                logger.debug("Cannot move to {0} {1}".format(self.x, self.y + move_val))
        # Move +1 if EAST and MOVE -1 if WEST
        elif self.facing == "WEST" or self.facing == "EAST":
            can_move = self.table.check_position(self.x + move_val, self.y)
            if can_move:
                logger.debug("Moving to {0} {1}".format(self.x, self.y))
                self.x = self.x + move_val
                return True
            else:
                logger.debug("Cannot move to {0} {1}".format(self.x + move_val, self.y))

        return False

    @check_has_placed
    def rotate(self, which: str):
        next_direction = None
        if which == "LEFT":
            next_direction = (DIRECTION[self.facing] + 1) % 4
        elif which == "RIGHT":
            next_direction = (DIRECTION[self.facing] - 1) % 4

        self.facing = INVERSE_DIRECTION[next_direction]

