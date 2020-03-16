import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.simulators import Entity, System
from src.units import Vector
from random import randrange

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
            entity1 = Entity(2)
            entity1.name = f"{x} {y}"
            wall_cache[f"{x} {y}"] = [0, 0]
            entity1.position = Vector(x-5, y-5)
            randomthings.append(entity1)

    entity1 = Entity(5)
    entity1.name = f"other"
    wall_cache[f"other"] = [0, 0]
    entity1.position = Vector(0, -7.5)
    entity1.velocity = Vector(-1, 1.2)
    randomthings.append(entity1)

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
