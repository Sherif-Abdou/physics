from ..units import Vector, Newton
from .motion import Motion


class Entity:
    def __init__(self, mass):
        self.__motion = Motion()
        self.mass = mass
        self.name = ""

    def apply_force(self, force):
        if isinstance(force, Newton):
            force.mass = self.mass
            self.__motion.acceleration += force.acceleration
        elif isinstance(force, Vector):
            self.__motion.acceleration += (force / self.mass)

    @property
    def position(self):
        return self.__motion.position

    @position.setter
    def position(self, value):
        self.__motion.position = value

    @property
    def time(self):
        return self.__motion.time

    @time.setter
    def time(self, value):
        self.__motion.time = value

    @property
    def velocity(self):
        return self.__motion.velocity

    @velocity.setter
    def velocity(self, value):
        self.__motion.velocity = value
