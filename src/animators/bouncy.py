import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.simulators import Entity, System
from src.units import Vector

wall_cache = dict()


def wall(system: System):
    for entity in system.entities:
        if system.time - wall_cache[entity.name][0] > 0.075:
            if abs(entity.position.x) > 10:
                entity.velocity.x *= -1
                wall_cache[entity.name][0] = system.time

        if system.time - wall_cache[entity.name][1] > 0.075:
            if abs(entity.position.y) > 10:
                entity.velocity.y *= -1
                wall_cache[entity.name][1] = system.time


if __name__ == "__main__":
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'ro')

    randomthings = []
    for x in range(5):
        for y in range(5):
            entity = Entity(2)
            entity.name = f"{x} {y}"
            wall_cache[f"{x} {y}"] = [0, 0]
            entity.position = Vector(2 * (x - 2.5), 2 * (y - 2.5))
            randomthings.append(entity)

    special_entity = Entity(8)
    special_entity.name = f"other"
    wall_cache[f"other"] = [0, 0]
    special_entity.position = Vector(-9, -9)
    special_entity.velocity = Vector(1, 2)
    randomthings.append(special_entity)

    system = System(randomthings)
    system.onUpdate = wall


    def init():
        ax.set_ylim(-10, 10)
        ax.set_xlim(-10, 10)
        return ln,


    def update(frame):
        system.time += 0.05
        xdata = []
        ydata = []
        for entity in system.entities:
            xdata.append(entity.position.x)
            ydata.append(entity.position.y)
        ln.set_data(xdata, ydata)
        return ln,


    ani = FuncAnimation(fig, update,
                        init_func=init, interval=50)
    plt.show()
