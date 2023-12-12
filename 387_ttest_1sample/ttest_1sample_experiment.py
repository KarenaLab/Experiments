# T-Test - 1 Sample from scratch [P387]
# 

# Libraries
import os
import sys

import numpy as np
import pandas as pd

import scipy.stats as st

import matplotlib.pyplot as plt


# Personal modules
sys.path.append(r"c:\python_modules")


# Functions
def better_sample(loc, scale, size, error="dynamic", decimals=6, seed=None,
                  maximum=10000, verbose=True):
    """
    Creates a Gaussian distribution sample using ´np.random.normal´ but
    controls the error from **mean** and **standard deviation**, keeping
    it closer to the gap controled by the **error**.

    """
    # Seed (optional)
    if(seed != None and isinstance(seed, int) == True):
        np.random.seed(seed)


    # Error
    if(error == "dynamic"):
        error = 0.001


    # Rolling the dice ;)
    i = 0

    while(True):
        sample = np.random.normal(loc=loc, scale=scale, size=size)
        sample = np.round(sample, decimals=decimals)

        sample_mean = np.mean(sample)
        sample_stddev = np.std(sample)

        # Test conditions
        if(sample_mean >= (loc - error) and sample_mean <= (loc + error) and
           sample_stddev >= (scale - error) and sample_stddev <= (scale + error)):
            break


        i = i + 1

        if(i == maximum):
            error_list = [0.001, 0.01, 0.1, 0.5, 1, 2, 5, 10, 20, 50, 100]

            try:
                pos = error_list.index(error)

            except ValueError:
                error = error_list[min(range(0, len(error_list)), key=lambda i: abs(error_list[i] - error))]
                pos = error_list.index(error)


            pos = pos + 1
            error = error_list[pos]
            i = 0

            if(verbose == True):
                print(f" > Message: Error range updated. {error=}")


    return sample


def gaussian_curve(loc, scale, size=1000, slide=4):
    """
    Returns x and y for a perfect gaussian curve fitted.
    Using the function: ´st.norm.pdf()`

    More info:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html

    """
    x = np.linspace(start=(loc - (slide * scale)), stop=(loc + (slide * scale)), num=size)
    y = st.norm.pdf(x, loc=loc, scale=scale)

    return x, y



# Setup/Config



# Program --------------------------------------------------------------
sample = better_sample(loc=5000, scale=70, size=10)



# end

