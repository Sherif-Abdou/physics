import unittest
from src import Vector, Motion


class VelocityTestCase(unittest.TestCase):
    def test_velocity(self):
        motion = Motion()
        motion.velocity = Vector(1, 1)
        self.assertEqual(motion.position.x, 0)
        motion.time = 2
        self.assertEqual(motion.position.x, 2)

    def test_velocity2(self):
        motion = Motion()
        motion.velocity = Vector(1, 1)
        for i in range(50):
            motion.time += 1
            self.assertEqual(motion.position.x, i + 1)
            self.assertEqual(motion.position.y, i + 1)


class AccelerationTestCase(unittest.TestCase):
    def test_acceleration(self):
        motion = Motion()
        motion.acceleration = Vector(2, 2)
        self.assertEqual(motion.position, Vector(0, 0))
        motion.time += 2
        self.assertEqual(motion.position, Vector(4, 4))

    def test_acceleration2(self):
        motion = Motion()
        motion.acceleration = Vector(2, 4)
        self.assertEqual(motion.position, Vector(0, 0))
        motion.time += 3
        self.assertEqual(motion.position, Vector(9, 18))


if __name__ == '__main__':
    unittest.main()
