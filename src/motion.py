from src.vector import Vector


class Motion:
    def __init__(self):
        self.position = Vector(0, 0)
        self.velocity = Vector(0, 0)
        self.__time = 0

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__applyVelocity(self.__time, value)
        self.__time = value

    def __applyVelocity(self, before, after):
        delta_time = after-before
        movement_vector = Vector(self.velocity.x * delta_time, self.velocity.y * delta_time)
        self.position = Vector(self.position.x + movement_vector.x, self.position.y + movement_vector.y)
