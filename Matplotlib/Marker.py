import matplotlib.pyplot as plt
import numpy as np

# marker together => marker|line|color
# marker reference => * (star), o (round filled), x (cross), X (cross filled), d (diamond), p (pentagon) etc.
# line reference => : (dotted), - (solid line), -- (dashed line), -. (dashed/dotted line)
# color reference => r, g, b (blue), c, m, y, k (black), w

# more??
# marker => marker = any marker literal
# marker size => ms = any number
# marker edge color => mec = any color liretal
# marker face color => mfc = any color liretal

# line width => linewidth = any number


def draw_diagram():
    x = np.array([1, 2, 6, 8, 10])
    y = np.array([3, 8, 1, 10, 5])

    plt.plot(x, y, 'o-.g', ms=12, mec='#4CAF50', mfc='#4CAF50', linewidth=3)


if __name__ == '__main__':
    draw_diagram()
    plt.show()
