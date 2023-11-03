import numpy as np
import matplotlib.pyplot as plt

grid = np.array([-1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1])
plt.imshow(grid.reshape(5, 5))
plt.savefig("matplotlib/grid.png")
