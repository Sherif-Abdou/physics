import unittest
from src.simulators import Entity
from src.units import Vector


class EntityTestCase(unittest.TestCase):
    def test_force(self):
        entity = Entity(1)
        entity.apply_force(Vector(2, 2))
        for i in range(10):
            self.assertEqual(entity.position, Vector(i**2, i**2))
            entity.time += 1


if __name__ == '__main__':
    unittest.main()
