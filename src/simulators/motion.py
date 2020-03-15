from src.units import Vector


class Motion:
    def __init__(self):
        self.position = Vector(0, 0)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.__time = 0

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__applyVelocity(self.__time, value)
        self.__time = value

    def __applyAcceleration(self, before, after):
        delta_time = after - before
        return (self.acceleration / 2) * (delta_time ** 2)

    def __applyVelocity(self, before, after):
        movement_vector = self.__calculateVelocity(after, before)
        self.position = self.position + movement_vector

    def __calculateVelocity(self, after, before):
        delta_time = after - before
        movement_vector = self.velocity * delta_time
        movement_vector += self.__applyAcceleration(before, after)
        self.velocity += self.acceleration
        return movement_vector
