import matplotlib.pyplot as plt
import numpy as np


def draw_line():
    x = np.array([8, 1, 10])
    y = np.array([10, 3, 5])

    plt.plot(x, y, marker='o')


def draw_diagram():
    x = np.array([1, 2, 6, 8, 10])
    y = np.array([3, 8, 1, 10, 5])

    plt.plot(x, y, marker='o')


if __name__ == '__main__':
    draw_line()
    draw_diagram()
    plt.show()
