from toy_car.utilities import check_has_placed

# Some static constance to handle turning

direction = {

    "NORTH": 1,
    "SOUTH": -1,
    "WEST": -1,
    "EAST": 1
}


class Car:
    """
    Base class for Car that can move in 2D grid.

    A car is given a 2D grid to drive on

    Function:
        Forward - Move forward
        Left - Move left
        Right - Move right
        Backward - Move backward

    """

    def __init__(self, table):
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

        self.has_placed = True

        self.x = x
        self.y = y

        # When placing facing/direction, check if those are keys in the direction dict declared above
        if facing in direction:
            self.facing = facing
        else:
            raise ValueError("Improper value for facing")

        print("A car has been placed at ({0}, {1}) and is facing {2}".format(self.x, self.y, self.facing))

    @check_has_placed
    def report(self):

        print("The car is at {0}, {1} and is facing {2}".format(self.x, self.y, self.facing))

    @check_has_placed
    def move(self):

        # Move +1 if NORTH MOVE -1 If SOUTH
        if self.facing == "NORTH" or self.facing == "SOUTH":
            move_val = direction[self.facing]
            can_move = self.table.check_position(self.x, self.y + move_val)
            if can_move:
                print("BEEP!! BEEP!!, MOVING {}".format(self.facing))
                self.y = self.y + move_val
            else:
                print("Cannot go to {0} {1} because the table is too small!!".format(self.x, self.y + move_val))

    @check_has_placed
    def rotate_south(self):

        # Testing only, will remove in the future
        self.facing = "SOUTH"

    # This function receive commands from the console, return an error message if wrong command is entered
    def compute_command(self, command: str, pos_x: int | None, pos_y: int | None):

        if command == "PLACE":

            output = self.place(pos_x, pos_y)

            return output

        elif command == "REPORT":

            self.report()

        else:

            return "Nothing happens"

