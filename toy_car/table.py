class Table:

    def __init__(self):

        # Set default width of this table to 5 and 5
        self.width = 5
        self.height = 5

        # This array marks where the car is at
        self.array_representation = [[0 for i in range(self.width)] for j in range(self.height)]

    def check_position(self, x, y):

        print(x, y)

        return x in range(0, self.width) and y in range(0, self.height)






