from .vector import Vector


class Newton:
    def __init__(self):
        self.acceleration = Vector(0, 0)
        self.mass = 0

    @classmethod
    def from_vector(cls, vector, mass):
        value = cls()
        value.acceleration /= mass
        value.mass = mass
        return value

    def to_vector(self):
        return self.acceleration * self.mass
