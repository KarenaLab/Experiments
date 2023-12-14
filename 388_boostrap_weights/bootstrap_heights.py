# Name [P388] Bootstrap with plympic weights of teams

# Libraries
import os
import sys

import numpy as np
import pandas as pd

import scipy.stats as st

import matplotlib.pyplot as plt


# Comments and information
#
# 1- Country 3 letters international code
#    https://en.wikipedia.org/wiki/ISO_3166-1


# Personal modules
sys.path.append(r"c:\python_modules")


# Functions
def read_csv(filename, sep=",", encoding="utf-8"):
    """
    Read and prepare the dataframe with weights.

    """
    data = pd.read_csv(filename, sep=sep, encoding=encoding)
    data = data.drop(columns=["Unnamed: 0"])

    data = data.rename(columns={"altura_guatemala": "guatemala",
                                "altura_holanda": "netherlands"})


    return data



# Setup/Config
filename = "alturas.csv"


# Program --------------------------------------------------------------

df = read_csv(filename)

ks_guatemala = st.kstest(df["guatemala"], "norm")
ks_netherlands = st.kstest(df["netherlands"], "norm")


# Bootstrap
df = df.melt(var_name="country", value_name="height_m")

# Country ISO Codes
# Guatemala = GT or GTM
# Netherlands = NL or NLD

# Lists for Bootstrap metrics store
mean_diff = np.array([])
mean_gt = np.array([])
mean_nl = np.array([])


for i in range(0, 5000):
    bootstrap = df.sample(n=24, replace=True)

    bs_mean_gt = bootstrap[bootstrap["country"] == "guatemala"]["height_m"].mean()
    #bs_stddev_gt = bootstrap[bootstrap["country"] == "guatemala"]["height_m"].std()
    bs_mean_nl = bootstrap[bootstrap["country"] == "netherlands"]["height_m"].mean()
    #bs_stddev_nl = bootstrap[bootstrap["country"] == "netherlands"]["height_m"].std()

    mean_diff = np.append(mean_diff, (bs_mean_nl - bs_mean_gt))
    mean_gt = np.append(mean_gt, bs_mean_gt)
    mean_nl = np.append(mean_nl, bs_mean_nl)


# 1 - Plot Guatemala and Netherlands

# 2 - Plot the difference

# 3 - Check between 2.5% and 97.5% (95% of CI)


# end

