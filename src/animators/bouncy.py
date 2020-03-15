import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from src.simulators import Entity, System
from src.units import Vector

if __name__ == "__main__":
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'ro')


    entity1 = Entity(1)
    entity1.name = "1"
    entity1.velocity = Vector(2, 2)

    entity2 = Entity(1)
    entity2.name = "2"
    entity2.velocity = Vector(-2, 2)
    entity2.position = Vector(10, 0)

    system = System([entity1, entity2])

    def init():
        ax.set_ylim(-10, 10)
        ax.set_xlim(-10, 10)
        return ln,


    def update(frame):
        system.time += 0.05
        xdata = [entity1.position.x, entity2.position.x]
        ydata = [entity1.position.y, entity2.position.y]
        ln.set_data(xdata, ydata)
        return ln,


    ani = FuncAnimation(fig, update,
                        init_func=init, interval=50)
    plt.show()
