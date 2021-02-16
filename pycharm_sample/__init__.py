def generate_list(*args):
    """ Silly function #1 """
    array = []
    for entry in args:
        array.append(entry)

    return array


def generate_dictionary(**kwargs):
    """ Silly function #2 """
    dictionary = {}
    for entry in kwargs:
        dictionary[entry] = kwargs[entry]

    return dictionary
