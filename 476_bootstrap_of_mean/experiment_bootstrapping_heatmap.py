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

size_space = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
repeat_space = [10, 20, 50, 100, 200, 500, 1000]

sample = data_split(data, size=np.max(repeat_space))

x, y = np.meshgrid(size_space, repeat_space)
z_mean, z_ci = list(), list()
for repeat in repeat_space:
    line_mean, line_ci = list(), list()
    for size in size_space:
        bs = bootstrap_with_mean(sample, size=size, repeat=repeat)
        mean = bs["bootstrap_mean"]
        ci_range = bs["ci_upper"] - bs["ci_lower"]
        line_mean.append(mean)
        line_ci.append(ci_range)

    z_mean.append(line_mean)
    z_ci.append(line_ci)


"""
sample = data_split(data, size=np.max(repeat_list))

mean_map = pd.DataFrame(data=[])
range_map = pd.DataFrame(data=[])

for size in size_list:   
    for repeat in repeat_list:
        bs = bootstrap_with_mean(sample, size=size, repeat=repeat)

        mean_map.loc[size, repeat] = bs["bootstrap_mean"]
        range_map.loc[size, repeat] = bs["ci_upper"] - bs["ci_lower"]
        
cs1 = plt.contour(x, y, z2, linewidths=0.5, colors='k')
cs2 = plt.contour(x, y, z2, cmap="RdBu_r")
plt.show()

"""
plt.imshow(z_ci, cmap='Blues', interpolation='nearest')
plt.show()






