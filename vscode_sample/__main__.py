from vscode_sample import create_2d_point, get_euclidian_distance

if __name__ == "__main__":
    print("Welcome to a buggy program.")
    p1 = create_2d_point(0, 0)
    p2 = create_2d_point(2, 2)
    print(get_euclidian_distance(p1, p2))
