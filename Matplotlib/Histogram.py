import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import size


def draw_hist():
    x = np.random.randint(120, size=50)
    plt.hist(x)


if __name__ == '__main__':
    draw_hist()
    plt.show()
