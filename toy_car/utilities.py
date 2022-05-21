# Decorator for car
def check_has_placed(f):
    def wrapper(*args):
        if args[0].has_placed:
            return f(*args)
        else:
            raise ValueError("Car has not been placed")
    return wrapper


# Check for positive integer
def check_positive_int(val: int):

    return val >= 0


