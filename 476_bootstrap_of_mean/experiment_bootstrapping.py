# [P475] Bootstrapping with the mean


# Libraries
import os
import sys

import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt


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
    print(sample_size)

    # Sample selection
    np.random.shuffle(data)
    sample = data[0: sample_size]


    return sample
    
    

# Program --------------------------------------------------------------
data = load_gaussian(mean=5, stddev=1, size=2000, seed=314)
pick = data_split(data, size=25)

bootstrap = bootstrap_with_mean(pick, size=10, repeat=200)
print(bootstrap)


# end
