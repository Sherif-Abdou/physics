from src.units import Vector


class Collision:
    def __init__(self, first, second, time):
        self.first = first
        self.second = second
        self.time = time


class System:
    continuous_interval = 0.008

    def __init__(self, entities):
        self.entities = entities
        self.__time = 0
        self.collision_range = 0.25
        self.__last_collision = None
        self.onUpdate = lambda system: ""

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        delta = (value - self.__time)
        times = int(delta // self.continuous_interval)
        for i in range(times):
            self.__time += self.continuous_interval
            self.__update()

        self.__time += delta - (self.continuous_interval * times)
        self.__update()

    def __update(self):
        for entity in self.entities:
            entity.time = self.time
        self.__check_collision()
        self.onUpdate(self)

    def __check_collision(self):
        last_hit1 = ""
        last_hit2 = ""
        for entity in self.entities:
            for other in self.entities:
                if entity.velocity == Vector(0, 0):
                    continue

                if other.name == entity.name or other.name == last_hit1 or entity.name == last_hit2:
                    continue

                if self.__last_collision is not None and (self.__last_collision.first == entity.name or self.__last_collision.first == other.name) and (self.__last_collision.second == entity.name or self.__last_collision.second == other.name):
                    if self.time - self.__last_collision.time < 0.1:
                        continue

                delta = (entity.position - other.position).mag
                if delta < self.collision_range:
                    self.__apply_collision(entity, other)
                    last_hit1 = entity.name
                    last_hit2 = other.name

    def __apply_collision(self, first, second):
        # x_equations = [((first.mass * first.velocity.x)+(second.mass * first.velocity.x)
        #                - (first.mass * v1) - (second.mass * v2)),
        #                (first.mass * first.velocity.x ** 2) + (second.mass * second.velocity.x ** 2)
        #                - (first.mass * v1**2) - (second.mass * v2**2)]
        #
        # y_equations = [((first.mass * first.velocity.y)+(second.mass * first.velocity.y)
        #                - (first.mass * v1) - (second.mass * v2)),
        #                (first.mass * first.velocity.y ** 2) + (second.mass * second.velocity.y ** 2)
        #                - (first.mass * v1**2) - (second.mass * v2**2)]
        #
        # x_values = nonlinsolve(x_equations, [v1, v2])
        # y_values = nonlinsolve(y_equations, [v1, v2])
        x_values = [(((first.mass - second.mass) * first.velocity.x) + (2 * second.mass * second.velocity.x)) /
                    (first.mass + second.mass), ((2 * first.mass * first.velocity.x)
                                                 - ((first.mass - second.mass)*second.velocity.x))]

        y_values = [(((first.mass - second.mass) * first.velocity.y) + (2 * second.mass * second.velocity.y)) /
                    (first.mass + second.mass), ((2 * first.mass * first.velocity.y)
                                                 - ((first.mass - second.mass) * second.velocity.y))]

        first.velocity = Vector(x_values[0], y_values[0])
        second.velocity = Vector(x_values[1], y_values[1])
        self.__last_collision = Collision(first.name, second.name, self.time)
        print(f"bop: f: {first.name} s: {second.name}")
