from . import generate_list, generate_dictionary

if __name__ == "__main__.py":
    sample_list = generate_list(1, 2, 3, 4, 5, 6, "potato", "hamburger", 9.0)

    # error
    sample_dict = generate_dictionary(sample_list)
