from toy_car.car import Car
from toy_car.table import Table

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

    # Allocate a car to a table, but the car has not been placed yet.
    table = Table()
    car = Car(table)

    while True:

        if not car.has_placed:

            placement_x = input('Please place a x position for your car')
            placement_y = input('Please place a y position for your car')
            placement_facing = input('What is the direction that your car is facing?')

            car.place(int(placement_x), int(placement_y), placement_facing)
            car.report()

        else:

            command = input("Input commands, MOVE, LEFT, RIGHT, REPORT")

            if command == "REPORT":

                car.report()

            elif command == "MOVE":

                car.move()

            elif command == "ROTATE":

                car.rotate_south()

            elif command == "EXIT":

                break

            else:
                print("Not yet implement")


if __name__ == '__main__':
    run_car()


