import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import sys

def python_example2(samples=10000):
    rng = np.random.default_rng()

    # Base 2D Gaussian dataset
    data = rng.normal(100, 6, (samples, 2))

    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # Panel 1: pure Gaussian
    axs[0,0].hist2d(data[:,0], data[:,1], bins=100, range=[[50,150],[50,150]], cmap='viridis')
    axs[0,0].set_title("2D Gaussian")

    # Panel 2: Gaussian + uniform offset
    data2 = np.vstack([data, rng.uniform(50,150,(samples//3,2))])
    axs[0,1].hist2d(data2[:,0], data2[:,1], bins=100, range=[[50,150],[50,150]], cmap='viridis')
    axs[0,1].set_title("2D Gaussian + offset")

    # Panel 3: Gaussian + baseline offset
    u = rng.uniform(0,1,samples*10)
    xvals = 1/(1-u*(1-1/11))*10 + 40
    yvals = rng.uniform(50,150, samples*10)
    data3 = np.vstack([data, np.column_stack([xvals, yvals])])
    axs[1,0].hist2d(data3[:,0], data3[:,1], bins=100, range=[[50,150],[50,150]],
                     cmap='viridis', norm=LogNorm())
    axs[1,0].set_title("2D Gaussian + offset2")

    # Panel 4: Double Gaussian
    data4 = np.vstack([data, rng.normal(100,20,(samples//2,2))])
    axs[1,1].hist2d(data4[:,0], data4[:,1], bins=100, range=[[50,150],[50,150]], cmap='viridis')
    axs[1,1].set_title("Double 2D Gaussian")

    fig.tight_layout()
    fig.savefig("canvas2d_py.png")

if __name__ == "__main__":
    samples = 10000
    if len(sys.argv) > 1:
        samples = int(sys.argv[1])
    python_example2(samples)

