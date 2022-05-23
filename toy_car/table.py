class Table:

    """
        5x5 grid table for the toy car to run on.
        The width (x) and the height (x) is hard coded as the exact width of the table 5x5 is given.

    """

    def __init__(self):

        # Set default width of this table to 5 and 5
        self.width = 5
        self.height = 5

    def check_position(self, x, y):

        return x in range(0, self.width) and y in range(0, self.height)






