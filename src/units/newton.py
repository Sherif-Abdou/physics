from .vector import Vector


class Newton:
    def __init__(self):
        self.acceleration = Vector(0, 0)
        self.__mass: float = 0

    @classmethod
    def from_vector(cls, vector, mass):
        value = cls()
        value.acceleration = vector
        value.acceleration /= mass
        value.__mass = mass
        return value

    def to_vector(self) -> Vector:
        return self.acceleration * self.mass

    @property
    def mass(self) -> float:
        return self.__mass

    @mass.setter
    def mass(self, value: float):
        full_acc = self.acceleration * self.mass
        self.acceleration = full_acc / value
        self.mass = value
