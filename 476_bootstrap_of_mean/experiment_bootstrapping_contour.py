# [P475] Bootstrapping with the mean


# Libraries
import os
import sys

import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt
import matplotlib.cm as cm


# Personal modules
sys.path.append("./src")
from bootstrap_mean import bootstrap_with_mean


# Setup/Config
path_main = os.getcwd()
path_report = os.path.join(path_main, "report")


# Functions
def load_gaussian(mean=0, stddev=1, size=1000, seed=None):
    """
    Creates a Gaussian (Normal) sample distribution with a given
    **mean (loc)** and **standard deviation (scale)** with a sample
    **size**.

    Optional: Inform **seed** for repeatability.

    """
    # Seed
    if(isinstance(seed, int) == True):
        np.random.seed(seed=seed)

    # Data
    data = np.random.normal(loc=mean, scale=stddev, size=size)


    return data


def data_split(data, size=25, seed=None):
    """
    Splits, or removes from **data** a given percentage informed with
    **size**.

    Optional: Inform **seed** for repeatability.

    """
    # Data preparation
    data = data.flatten()
    sample_size = int(data.shape[0] * (size / 100))

    # Sample selection
    np.random.shuffle(data)
    sample = data[0: sample_size]


    return sample


def apply_minmax(array):
    # Information
    x_min = np.min(array)
    x_max = np.max(array)

    transformed = list()
    for i in range(0, array.shape[0]):
        line = list()
        for j in range(0, array.shape[1]):
            value = (array[i][j] - x_min) / (x_max - x_min)
            line.append(value)

        transformed.append(line)

    transformed = np.array(transformed)

    return transformed

  
# Program --------------------------------------------------------------
data = load_gaussian(mean=50, stddev=5, size=2000, seed=314)

size_space = np.linspace(start=1, stop=15, num=15, dtype=int)
repeat_space = np.linspace(start=5, stop=50, num=10, dtype=int)

sample = data_split(data, size=np.max(repeat_space))

mean_map = pd.DataFrame(data=[])
range_map = pd.DataFrame(data=[])

for size in size_space:   
    for repeat in repeat_space:
        bs = bootstrap_with_mean(sample, size=size, repeat=repeat)

        mean_map.loc[size, repeat] = bs["bootstrap_mean"]
        range_map.loc[size, repeat] = bs["ci_upper"] - bs["ci_lower"]


x, y = np.meshgrid(range_map.index, range_map.columns)
z = np.array(range_map).T

# Plot
# Plot config
plt.rcParams["font.family"] = "Helvetica"
plt.rcParams["font.size"] = 8
plt.rcParams["figure.dpi"] = 120
plt.rcParams["ps.papersize"] = "A4"
plt.rcParams["xtick.direction"] = "inout"
plt.rcParams["ytick.direction"] = "inout"
plt.rcParams["xtick.major.size"] = 3.5
plt.rcParams["ytick.major.size"] = 3.5

# Plot figure 
fig = plt.figure(figsize=[8, 4.5])
fig.suptitle("Bootstrap - Countour of the Interval Confidence range",
             fontweight="bold", x=0.98, ha="right")

cs1 = plt.contour(x, y, z, linewidths=0.5, colors='k')
cs2 = plt.contour(x, y, z, cmap="RdBu_r")
plt.clabel(cs1, fontsize=7)

plt.xlabel("percentage of sub-sample size (%)", loc="right")
plt.ylabel("Number of repetitions (r)", loc="top")


plt.show()

