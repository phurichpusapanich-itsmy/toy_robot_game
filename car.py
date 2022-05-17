
def check_has_placed(f):
    def wrapper(*args):

        if args[0].has_placed:
            return f(*args)
        else:
            raise ValueError("Car has not been placed")
    return wrapper


class Car:
    """
    Base class for Car that can move in 2D grid.
    Function:
        Forward - Move forward
        Left - Move left
        Right - Move right
        Backward - Move backward
    """

    def __init__(self):
        self.has_placed = False
        self.x = None
        self.y = None
        self.facing = None

    def place(self, x: int, y: int, facing: str):

        # This is is an input, we need to enforce int here
        if not isinstance(x, int):
            raise TypeError("bar must be set to an integer")
        if not isinstance(y, int):
            raise TypeError("bar must be set to an integer")

        self.has_placed = True

        self.x = x
        self.y = y
        self.facing = facing

        print("A car has been placed at ({0}, {1}) and is facing {2}".format(self.x, self.y, self.facing))

    @check_has_placed
    def report(self):

        print("The car is at {0}, {1} and is facing {2}".format(self.x, self.y, self.facing))

    # This function receive commands from the console, return an error message if wrong command is entered
    def compute_command(self, command: str, pos_x: int | None, pos_y: int | None):

        if command == "PLACE":

            output = self.place(pos_x, pos_y)

            return output

        elif command == "REPORT":

            self.report()

        else:

            return "Nothing happens"

