# [P475] Bootstrapping with the mean


# Libraries
import os

import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt


# Personal modules
from bootstrap_mean import bootstrap_with_mean


# Functions
def load_gaussian(mean=0, stddev=1, size=1000, seed=None):
    """


    """
    # Seed
    if(isinstance(seed, int) == True):
        np.random.seed(seed=seed)

    # Data
    data = np.random.normal(loc=mean, scale=stddev, size=size)


    return data


def data_split(data, size=25, seed=None):
    """


    """
    # Data preparation
    data = data.flatten()
    sample_size = int(data.shape[0] * (size / 100))
    print(sample_size)

    # Sample selection
    np.random.shuffle(data)
    sample = data[0: sample_size]


    return sample
    
    

# Setup/Config



# Program --------------------------------------------------------------
data = load_gaussian(mean=5, stddev=1, size=2000, seed=314)
pick = data_split(data, size=25)

bootstrap = bootstrap_with_mean(pick, size=10, repeat=200)
print(bootstrap)


# end
