from src.units import Vector
from ..simulators import Entity


class System:
    # The interval that the system should update at
    continuous_interval = 0.008

    def __init__(self, entities):
        self.entities: list[Entity] = entities
        self.__time: float = 0
        # The distance between two objects for them to collide
        self.collision_range = 0.25
        self.onUpdate = lambda system: ""

    @property
    def time(self) -> float:
        return self.__time

    @time.setter
    def time(self, value: float):
        delta = (value - self.__time)
        # Update time separately for each continuous_interval in delta
        times = int(delta // self.continuous_interval)
        for i in range(times):
            self.__time += self.continuous_interval
            self.__update()

        # Update time for the remainder amount
        self.__time += delta - (self.continuous_interval * times)
        self.__update()

    def __update(self):
        for entity in self.entities:
            entity.time = self.time
        self.__check_collision()
        self.onUpdate(self)

    def __check_collision(self):
        last_hit_name1 = ""
        last_hit_name2 = ""
        for entity in self.entities:
            for other in self.entities:
                # Objects sitting still can't start a collision
                if entity.velocity == Vector(0, 0):
                    continue

                # Prevents a and b from colliding then b and a colliding again
                if other.name == entity.name or other.name == last_hit_name1 or entity.name == last_hit_name2:
                    continue

                # If the two entities are in range, trigger a collision
                delta = (entity.position - other.position).mag
                if delta < self.collision_range:
                    self.__apply_collision(entity, other)
                    last_hit_name1 = entity.name
                    last_hit_name2 = other.name

    def __apply_collision(self, first, second):
        # Collision formulas from Wikipedia
        v1 = first.velocity - (first.position - second.position) * ((2 * second.mass) / (first.mass + second.mass)) * (
                    ((first.velocity - second.velocity) * (first.position - second.position)) / (
                        first.position - second.position).mag ** 2)
        v2 = second.velocity - (second.position - first.position) * ((2 * first.mass) / (first.mass + second.mass)) * (
                    ((second.velocity - first.velocity) * (second.position - first.position)) / (
                        second.position - first.position).mag ** 2)

        first.velocity = v1
        second.velocity = v2
