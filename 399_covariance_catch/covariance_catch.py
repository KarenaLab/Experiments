# Name [Pxxx]
# (optional) Short description of the program/module.


# Libraries
import os
import sys
from collections import namedtuple

import numpy as np
import pandas as pd
import scipy.stats as st

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt


# Personal modules
sys.path.append(r"c:\python_modules")


# Functions
def dataset1():
    """
    Returns x and y for a given dataset.

    """
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([2.1, 4.2, 5.9, 8.4, 9.9, 12.6, 14.5, 16.9, 18.2, 20])

    return x, y


def dataset1():
    """
    Returns x and y for a given dataset.

    """
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([2.1, 3.5, 5.8, 8.9, 10.5, 13.9, 14.9, 18.5, 18.9, 20])

    return x, y


def linreg_deg1(x, y):
    """
    Estimates a Linear Regression with degree one for a given **x** and
    **y**.

    """


def regr_metrics(y_true, y_pred, decimals=6):
    """
    Returns metrics for a regression model.
    Returns a tuple with: MAE, RMSE, and Pearson R.

    """
    results = namedtuple("metrics", ["MAE", "RMSE", "Pearson"])

    mae = np.round(mean_absolute_error(y_true, y_pred), decimals=decimals)
    rmse = np.round(mean_squared_error(y_true, y_pred, squared=True), decimals=decimals)
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
    calc = ((start - end) / end) * 100

    return calc

    

# Program --------------------------------------------------------------




# end

