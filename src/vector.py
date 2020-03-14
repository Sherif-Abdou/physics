import math


class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def mag(self):
        return math.hypot(self.x, self.y)

    @mag.setter
    def mag(self, mag):
        prev_angle = self.angle
        self.x = math.cos(prev_angle)*mag
        self.y = math.sin(prev_angle)*mag

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    @angle.setter
    def angle(self, angle):
        prev_mag = self.mag
        self.x = math.cos(angle) * prev_mag
        self.y = math.sin(angle) * prev_mag
