import unittest
from vscode_sample import create_2d_point, get_euclidian_distance


class testVsCodeSample(unittest.TestCase):
    def setUp(self):
        self.p1 = create_2d_point(0, 0)
        self.p2 = create_2d_point(2, 2)
        self.p3 = create_2d_point(1, 1)

    def test_euclidian_distance(self):
        """
        Test whether the correct Euclidian distance is returned.
        """

        self.assertAlmostEqual(1.41421356237, get_euclidian_distance(self.p1, self.p3))
        self.assertAlmostEqual(1.41421356237, get_euclidian_distance(self.p2, self.p3))

        self.assertAlmostEqual(2.82842712475, get_euclidian_distance(self.p2, self.p1))


if __name__ == "__main__":
    unittest.main()
