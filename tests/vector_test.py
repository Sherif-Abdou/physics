import unittest
from math import sqrt, radians
from src import Vector


class VectorTests(unittest.TestCase):
    def test_init(self):
        vector = Vector(1, 2)
        print(vector)
        self.assertEqual(vector.x, 1)
        self.assertEqual(vector.y, 2)

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
        self.assertAlmostEqual(vector.angle, radians(45) / 2, delta=0.01)


if __name__ == '__main__':
    unittest.main()
