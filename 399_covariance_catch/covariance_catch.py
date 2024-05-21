# Covariance Catch [P399]
# Short experiment to show the difference that covariance has and its
# dataset.

# Libraries
import os
import sys
from collections import namedtuple

import numpy as np
import pandas as pd
import scipy.stats as st

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt


# Personal modules
sys.path.append(r"c:\python_modules")


# Functions
def load_dataset1():
    """
    Returns x and y for a given dataset.

    """
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([2.1, 4.2, 5.9, 8.4, 9.9, 12.6, 14.5, 16.9, 18.2, 20])

    return x, y


def load_dataset2():
    """
    Returns x and y for a given dataset.

    """
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([2.1, 3.5, 5.8, 8.9, 10.5, 13.9, 14.9, 18.5, 18.9, 20])

    return x, y


def linreg_deg1(x, y, decimals=6):
    """
    Estimates a Linear Regression with degree one for a given **x** and
    **y**.

    """
    b, a = np.polyfit(x, y, deg=1)      # Equation = a + b*x
    y_hat = np.round([a + b * i for i in x], decimals=decimals)

    return y_hat


def regr_metrics(y_true, y_pred, decimals=6):
    """
    Returns metrics for a regression model.
    Returns a tuple with: MAE, RMSE, and Pearson R.

    """
    results = namedtuple("metrics", ["mae", "rmse", "pearson"])

    mae = np.round(mean_absolute_error(y_true, y_pred), decimals=decimals)
    rmse = np.round(root_mean_squared_error(y_true, y_pred), decimals=decimals)
    pearson = np.round(st.pearsonr(y_true, y_pred).statistic, decimals=decimals)

    metrics = results(mae, rmse, pearson)

    return metrics


def var_pct(start, end):
    """
    Calculates the variation percentual.

                     (start - end)
    Equation = d% = --------------- * 100
                           end

    """
    calc = ((end - start) / start) * 100

    return calc

    

# Program --------------------------------------------------------------

# Load datasets
x1, y1 = load_dataset1()
x2, y2 = load_dataset2()

# Fit Linear Regression (deg=1) and its metrics (MAE, RMSE, Pearson)
y1_pred = linreg_deg1(x1, y1)
y2_pred = linreg_deg1(x2, y2)

results1 = regr_metrics(y1, y1_pred)
results2 = regr_metrics(y2, y2_pred)

# Covariance
cov1 = np.cov(x1, y1)[1,0]
cov2 = np.cov(x2, y2)[1,0]

# Variation of differences
print(f" >    Variation of differences for Pearson: {var_pct(results1.pearson, results2.pearson):+.4f}")
print(f" > Variation of differences for Covariance: {var_pct(cov1, cov2):+.4f}")

# end
