import matplotlib.pyplot as plt
import numpy as np
from numpy.core.defchararray import title
from numpy.core.fromnumeric import size


def draw_pie():
    y = np.random.randint(8, size=5)

    parcent = [round((x*100)//np.sum(y)) for x in y]

    colors = ['red', 'green', 'cyan', 'pink', 'magenta']
    labels = np.array([f'{colors[i]} {parcent[i]}' for i in range(len(y))])
    explodes = np.array([0.2, 0, 0, 0, 0])

    plt.pie(y, colors=colors, labels=labels, explode=explodes, shadow=True, startangle=0)
    # plt.legend(title='Five color')


if __name__ == '__main__':
    draw_pie()
    plt.show()
