import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import size


def draw_scatter():
    x = np.random.randint(20, size=8)
    y = np.random.randint(50, size=8)
    colors = np.array(['red', 'green', 'black', 'hotpink', 'yellow', 'blue', 'pink', 'magenta'])
    # plt.scatter(x, y)
    plt.scatter(x, y, c=colors)
    plt.grid()


def compare_plots():
    x = np.random.randint(20, size=20)
    y = np.random.randint(50, size=20)
    plt.scatter(x, y, color='red')

    x = np.random.randint(20, size=20)
    y = np.random.randint(50, size=20)
    plt.scatter(x, y, color='green')


if __name__ == '__main__':
    # draw_scatter()
    compare_plots()
    plt.show()
