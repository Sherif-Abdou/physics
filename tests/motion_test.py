import unittest
from src import Vector, Motion


class MyTestCase(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
