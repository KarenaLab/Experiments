# Libraries
import numpy as np
import matplotlib.pyplot as plt


# Functions
def binning_sqrt(n):
    h = np.sqrt(n)
    h = int(h + 0.5)

    return h


def binning_sturges(n):
    h = np.log2(n) + 1
    h = int(h + 0.5)

    return h


def binning_rice(n):
    h = 2 * n ** (1/3)
    h = int(h + 0.5)

    return h


# Program
size = [10, 20, 50, 100, 200, 500, 1000]

sqrt_list = list(map(binning_sqrt, size))
sturges_list = list(map(binning_sturges, size))
rice_list = list(map(binning_rice, size))


# Plot
fig = plt.figure(figsize=[8, 4.5])
title = "Binning strategies N"
plt.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

plt.plot(size, sqrt_list, color="darkblue", label="sqrt", zorder=20)
plt.plot(size, sturges_list, color="darkred", label="sturges", zorder=21)
plt.plot(size, rice_list, color="darkgreen", label="rice", zorder=22)

plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)
plt.ylabel("number of bins (h)", loc="top")
plt.xlabel("dataset sample size (n)", loc="right")
plt.legend(loc="upper left", framealpha=1)

plt.tight_layout()
plt.savefig(title, dpi=240)
plt.show()
