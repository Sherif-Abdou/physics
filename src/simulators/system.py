from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve

class System:
    continuous_interval = 0.1

    def __init__(self, entities):
        self.entities = entities
        self.__time = 0
        self.collision_range = 0.25

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        delta = (value-self.__time)
        times = int(delta // self.continuous_interval)
        for i in range(times):
            self.__time += 0.1
            self.__update()

        self.__time += delta - (self.continuous_interval * times)
        self.__update()

    def __update(self):
        for entity in self.entities:
            entity.time = self.time

    def __check_collision(self):
        for entity in self.entities:
            for other in self.entities:
                if other.name == entity.name:
                    continue

                delta = entity.position - other.position
                if delta < self.collision_range:
                    pass

    def __apply_collision(self, first, second):
        pass
