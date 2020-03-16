import unittest
from src.simulators import System, Entity
from src.units import Vector


class SystemTestCase(unittest.TestCase):
    def test_system(self):
        entity1 = Entity(1)
        system = System([entity1])

        system.entities[0].apply_force(Vector(1, 1))
        system.time += 3
        self.assertAlmostEqual(system.entities[0].position.x, 4.5, delta=0.001)
        self.assertAlmostEqual(system.entities[0].position.y, 4.5, delta=0.001)
        self.assertAlmostEqual(system.time, 3, delta=0.001)

    def test_collision(self):
        entity1 = Entity(1)
        entity1.name = "1"
        entity1.velocity = Vector(1, 0)

        entity2 = Entity(1)
        entity2.name = "2"
        entity2.velocity = Vector(-1, 0)
        entity2.position = Vector(10, 0)

        system = System([entity1, entity2])
        system.time += 10
        print(entity1.position)
        print(entity2.position)


if __name__ == '__main__':
    unittest.main()
