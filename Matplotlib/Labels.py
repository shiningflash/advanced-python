import matplotlib.pyplot as plt
import numpy as np


def get_font(title=False):
    return {
        'family': 'ubuntu',
        'color': 'blue',
        'size': 20 if title else 10
    }


def show_diagram():
    x = np.array([1, 2, 4, 7])
    y = np.array([3, 1, 9, 5])

    plt.plot(x, y, 'o-.b')

    plt.title('This is title', fontdict=get_font(title=True), loc='left')
    plt.xlabel('This is x-label', fontdict=get_font())
    plt.ylabel('This is y-label', fontdict=get_font())

    plt.grid(color='green', linestyle='--', linewidth=.5)


if __name__ == '__main__':
    show_diagram()
    plt.show()
