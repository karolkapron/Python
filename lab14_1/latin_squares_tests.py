import unittest
from latin_squares import *
import numpy as np


class LatinSquareTests(unittest.TestCase):


    def test_is_latin(self):
        latin_array = [[1, 4, 2, 3], [3, 2, 4, 1], [2, 3, 1, 4], [4, 1, 3, 2]]
        no_latin_array = [[3, 2, 1, 4], [1, 2, 3, 4], [2, 4, 3, 1], [4, 3, 2, 2]]

        first = is_latin(latin_array)
        second = is_latin(no_latin_array)
        self.assertEqual(first, True)
        self.assertEqual(second, False)


    def test_Latin_square(self):

        n = 5

        ls = np.array(latin_square(n))
        rows, cols = ls.shape
        self.assertEqual(rows, n)
        self.assertEqual(cols, n)

        result = is_latin(ls)

        self.assertEqual(result, True)



if __name__ == '__main__':
    unittest.main()