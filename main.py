from car import Car

"""
    This is a 5x5 table top, 
        - 0 = No car
        - 1 = Has car
"""

table_top = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


def run_car():

    car = Car()

    max_index = len(table_top) - 1

    while True:

        if not car.has_placed:

            placement_x = input('Please place a x position for your car')
            placement_y = input('Please place a y position for your car')
            placement_facing = input('What is the direction that your car is facing?')

            # We have to check first if the car can be placed or not.
            try:
                # To represent X Y coordinate in Python, we need to think that array[x][y] is actually array[y][x]
                # Given that array 0, 0 is at south west, then it is array[len(array) - y][x]
                table_top[max_index - int(placement_y)][int(placement_x)] = 1
                car.place(int(placement_x), int(placement_y), placement_facing)

                print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in table_top]))

            except (ValueError, IndexError):
                print("Cannot place car in this position")

        else:

            command = input("Input commands, MOVE, LEFT, RIGHT, REPORT")

            if command == "REPORT":

                print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in table_top]))

                car.report()

            # Try moving up only
            elif command == "MOVE":

                # Treat negative as not being able to move
                if max_index - int(car.y) - 1 < 0:
                    print("Cannot move")
                else:
                    try:
                        table_top[max_index - int(car.y)][int(car.x)] = 0
                        table_top[max_index - int(car.y) - 1][int(car.x)] = 1
                        car.place(int(car.x), int(car.y) + 1, "NORTH")
                    except (ValueError, IndexError):
                        print("Cannot move")

            elif command == "EXIT":

                break

            else:
                print("Not yet implement")


if __name__ == '__main__':
    run_car()


