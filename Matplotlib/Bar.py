import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import size


def draw_bar():
    x = np.array(['A', 'B', 'C', 'D', 'E'])
    y = np.random.randint(12, size=5)
    plt.bar(x, y, color='blue', width=.6) # vertical
    # plt.barh(x, y, color='blue', height=.6) # horizontal


if __name__ == '__main__':
    draw_bar()
    plt.show()
