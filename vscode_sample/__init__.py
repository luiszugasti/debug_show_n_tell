import pandas as pd
import math

# globals
__version__ = "0.1.0"
TOLERANT_DIVERGENCE = 0.0000001


def get_square_root(a, x):
    """ Recursively computes the square root """
    new_x = (x + a / x) / 2
    if math.fabs(x - new_x) < TOLERANT_DIVERGENCE:
        return new_x

    return get_square_root(a, new_x)


def get_euclidian_distance(row1, row2):
    """ Returns 2 dimensional euclidian distance between two rows of a dataframe """

    intermediate_y = math.fabs(int(row1["y"]) - int(row2["y"]))
    intermediate_x = math.fabs(int(row1["x"]) - int(row2["x"]))

    return get_square_root(intermediate_x ** 2 + intermediate_y ** 2, 1.0)


def create_2d_point(x, y):
    return pd.DataFrame({"x": [x], "y": [y]})
