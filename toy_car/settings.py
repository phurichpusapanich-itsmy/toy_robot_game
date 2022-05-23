# The name of the application
APP_NAME = "toy_robot_challenge"

# List of valid car commands
LIST_OF_CAR_COMMANDS = ('MOVE', 'REPORT', 'LEFT', 'RIGHT', 'PLACE')

# Direction and its corresponding sequence value similar to Cardinal Direction
DIRECTION = {

    'NORTH': 0,
    'WEST': 1,
    'SOUTH': 2,
    'EAST': 3

}

# Direction movement setting
DIRECTION_MOVE_VALUES = {

    'NORTH': 1,
    'SOUTH': -1,
    'EAST': 1,
    'WEST': -1

}
# Inverted DIRECTION dictionary to help with re-grabing the key
INVERSE_DIRECTION = {v: k for k, v in DIRECTION.items()}

