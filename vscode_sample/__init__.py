import pandas as pd
import math

# globals
__version__ = "0.1.0"
TOLERANT_DIVERGENCE = 0.0001


def get_square_root(a, x):
    """ Recursively computes the square root """
    new_x = (x + a / x) // 2
    if math.fabs(x - new_x) < TOLERANT_DIVERGENCE:
        return new_x

    return get_square_root(a, new_x)


def get_euclidian_distance(row1, row2):
    """ Returns 2 dimensional euclidian distance between two rows of a dataframe """

    # Consider, for a moment, that we didn't know _what_was happening with our program.
    # we could try print statements.
    print("row1's x entry: {}, row1's y entry: {}".format(row1["x"], row1["y"]))

    # print statements are potentially brittle, depending on how much they expect from a data structure/API
    print("row2's x entry: {}, row2's y entry: {}".format(row1["X"], row1["Y"]))

    intermediate_y = row1["y"] ** 2 - row2["y"] ** 2
    intermediate_x = row1["x"] ** 2 - row2["x"] ** 2

    intermediate_y = int(row1["y"]) - int(row2["y"])
    intermediate_x = int(row1["x"]) - int(row2["x"])

    return get_square_root(intermediate_x + intermediate_y, 1.0)


def create_2d_point(x, y):
    return pd.DataFrame({"x": [x], "y": [y]})
