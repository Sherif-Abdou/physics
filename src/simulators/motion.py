from src.units import Vector


# Handles velocity and acceleration for a position
class Motion:
    def __init__(self):
        self.position: Vector = Vector(0, 0)
        self.velocity: Vector = Vector(0, 0)
        self.acceleration: Vector = Vector(0, 0)
        self.__time: float = 0

    @property
    def time(self) -> float:
        return self.__time

    @time.setter
    def time(self, value: float):
        self.__applyVelocity(self.__time, value)
        self.__time = value

    def __applyAcceleration(self, before, after):
        time_delta = after - before
        # Based on displacement formula for acceleration
        return (self.acceleration / 2) * (time_delta ** 2)

    def __applyVelocity(self, before, after):
        movement_vector = self.__calculateVelocity(after, before)
        self.position = self.position + movement_vector

    def __calculateVelocity(self, after, before):
        time_delta = after - before
        movement_vector = self.velocity * time_delta
        movement_vector += self.__applyAcceleration(before, after)
        self.velocity += self.acceleration * time_delta
        return movement_vector
