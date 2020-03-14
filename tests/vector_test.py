import unittest
from src.vector import *
from math import sqrt, radians


class VectorTests(unittest.TestCase):
    def test_init(self):
        vector = Vector(1, 2)
        print(vector)

    def test_magnitude(self):
        vector = Vector(1, 1)
        self.assertEqual(vector.mag, sqrt(2))
        self.assertAlmostEqual(vector.angle, radians(45), delta=0.01)
        vector.mag *= 2
        self.assertEqual(vector.mag, sqrt(8))
        self.assertAlmostEqual(vector.angle, radians(45), delta=0.01)

    def test_angle(self):
        vector = Vector(1, 1)
        self.assertEqual(vector.mag, sqrt(2))
        self.assertAlmostEqual(vector.angle, radians(45), delta=0.01)
        vector.angle = vector.angle / 2
        self.assertEqual(vector.mag, sqrt(2))
        self.assertAlmostEqual(vector.angle, radians(45)/2, delta=0.01)

if __name__ == '__main__':
    unittest.main()
