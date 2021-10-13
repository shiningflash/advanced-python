import math

import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import size


def draw_subplot():
    titles = ['sales', 'income', 'source', 'salary', 'budget']
    column = 3
    row = len(titles) // column + 1

    for i in range(len(titles)):
        x = np.random.randint(8, size=5)
        y = np.random.randint(12, size=5)
        plt.subplot(row, column, i+1)
        plt.plot(x, y)
        plt.grid()
        plt.title(titles[i])


if __name__ == '__main__':
    draw_subplot()
    plt.suptitle('bank information')
    plt.show()
