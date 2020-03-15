from .vector import Vector


class Newton:
    def __init__(self):
        self.acceleration = Vector(0, 0)
        self.__mass = 0

    @classmethod
    def from_vector(cls, vector, mass):
        value = cls()
        value.acceleration /= mass
        value.__mass = mass
        return value

    def to_vector(self):
        return self.acceleration * self.mass

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, value):
        full_acc = self.acceleration * self.mass
        self.acceleration = full_acc / value
        self.mass = value
