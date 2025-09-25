import numpy as np
import matplotlib.pyplot as plt

def plot_with_errors(ax, data, bins, range_, title, logy=False):
    # Compute histogram
    counts, edges = np.histogram(data, bins=bins, range=range_)
    centers = 0.5 * (edges[:-1] + edges[1:])
    errors = np.sqrt(counts)  # Poisson errors

    # Draw histogram as step
    ax.step(centers, counts, where='mid', color='black')
    # Add error bars
    ax.errorbar(centers, counts, yerr=errors, fmt='o', color='red', markersize=3)

    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("frequency")
    if logy:
        ax.set_yscale("log")

def main(samples=10000):
    np.random.seed(0)  # reproducibility

    # Gaussian
    mean1, sigma1 = 100, 6
    hist1_data = np.random.normal(mean1, sigma1, samples)

    # Canvas 1: single histogram with errors
    fig1, ax1 = plt.subplots(figsize=(6,4))
    plot_with_errors(ax1, hist1_data, bins=100, range_=(50,150), title="Random Gauss")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("canvas1_py.png")
    plt.close()

    # Canvas 2: 2x2 subplots
    fig, axs = plt.subplots(2,2, figsize=(10,8))

    # Subplot 1: Gaussian
    plot_with_errors(axs[0,0], hist1_data, bins=100, range_=(50,150), title="Random Gauss")

    # Subplot 2: Gaussian + uniform offset
    hist2_data = np.append(hist1_data, np.random.uniform(50,150, samples//3))
    plot_with_errors(axs[0,1], hist2_data, bins=100, range_=(50,150), title="Gauss + offset")

    # Subplot 3: Gaussian + 1/x^2 baseline
    hist3_data = np.copy(hist1_data)
    x = np.linspace(1,11,100000)
    p = 1/x**2
    p /= p.sum()
    hist3_data = np.append(hist3_data, np.random.choice(x*10+40, size=samples*30, p=p))
    plot_with_errors(axs[1,0], hist3_data, bins=100, range_=(50,150), title="Gauss + offset2", logy=True)

    # Subplot 4: Double Gaussian
    hist4_data = np.append(hist1_data, np.random.normal(mean1, 20, samples//2))
    plot_with_errors(axs[1,1], hist4_data, bins=100, range_=(50,150), title="Double Gaussian")

    plt.tight_layout()
    plt.savefig("canvas2_py.pdf")
    plt.close()

if __name__ == "__main__":
    main()

