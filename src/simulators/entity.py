from ..units import Vector, Newton
from .motion import Motion


# A physical object with its own motion system and mass
# Allows for forces to be applied
class Entity:
    def __init__(self, mass):
        self.__motion = Motion()
        self.mass = mass
        self.name: str = ""

    def apply_force(self, force):
        if isinstance(force, Newton):
            force.mass = self.mass
            self.__motion.acceleration += force.acceleration
        elif isinstance(force, Vector):
            self.__motion.acceleration += (force / self.mass)

    @property
    def position(self) -> Vector:
        return self.__motion.position

    @position.setter
    def position(self, value: Vector):
        self.__motion.position = value

    @property
    def time(self) -> float:
        return self.__motion.time

    @time.setter
    def time(self, value: float):
        self.__motion.time = value

    @property
    def velocity(self) -> Vector:
        return self.__motion.velocity

    @velocity.setter
    def velocity(self, value: Vector):
        self.__motion.velocity = value
