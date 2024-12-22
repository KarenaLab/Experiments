# [P449] Smoothing techniques
#

# Versions
# 01 - Dec 22rd, 2024 - Starter


# Libraries
import numpy as np
import pandas as pd


# ----------------------------------------------------------------------
def moving_average(Series, window):
    """
    Performs the moving average with a given **window**.

    """
    data = Series.rolling(window=window).mean()

    return data

    
# moving average

# exponential smoothing

# holt_winters

# lowess_smoothing

# kalman_filter

# savitzky_golay
