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

  
# Program --------------------------------------------------------------
data = load_gaussian(mean=50, stddev=5, size=2000, seed=314)

repeat_space = np.linspace(start=10, stop=90, num=9, dtype=int)
repeat_space = np.append(repeat_space, np.linspace(start=100, stop=1000, num=10, dtype=int))

sample = data_split(data, size=np.max(repeat_space))

df = pd.DataFrame(data=[])
for repeat in repeat_space:
    bs = bootstrap_with_mean(sample, size=50, repeat=repeat)

    df.loc[repeat, "mean"] = bs["bootstrap_mean"]
    df.loc[repeat, "ci_lower"] = bs["ci_lower"]
    df.loc[repeat, "ci_upper"] = bs["ci_upper"]
    df.loc[repeat, "ci_range"] = bs["ci_upper"] - bs["ci_lower"]

