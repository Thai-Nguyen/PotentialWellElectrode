import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Parameters
    max_iterations = int(1e3)

    # Define dimensions of simulation space
    h = 1
    x = np.arange(0, 122, h)
    y = np.arange(0, 102, h)

    # Make grid
    sim_space = np.meshgrid(x, y)

    # Allocate memory for storing potential function and give initial values
    V = 50 * np.ones((np.size(x), np.size(y)))

    # Calculate
    for iter in range(max_iterations):
        for i in range(np.size(x) - 1):
            for j in range(np.size(y) - 1):
                # Maintain voltage at electrodes
                V[11:111, 0:1] = 100
                V[0:1, 1:122] = 0
                V[121:122, 1:122] = 0
                V[1:121, 101:102] = 0
                # Traverse mesh and update
                V[i, j] = (V[i+1, j] + V[i-1, j] + V[i, j+1] + V[i, j-1]) / 4
        print('Iteration:', iter)

    V = np.transpose(V)
    plt.contourf(x, y, V)
    cs = plt.pcolor(V)
    plt.colorbar(cs)
    plt.savefig('potential_plot.png')
    plt.show()
