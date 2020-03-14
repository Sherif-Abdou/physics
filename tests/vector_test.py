import unittest
from src.vector import *
from math import sqrt


class VectorTests(unittest.TestCase):
    def test_init(self):
        vector = Vector(1, 2)
        print(vector)

    def test_magnitude(self):
        vector = Vector(1, 1)
        self.assertEqual(vector.mag, sqrt(2))
        vector.mag *= 2
        self.assertAlmostEqual(vector.mag, sqrt(8))

if __name__ == '__main__':
    unittest.main()
