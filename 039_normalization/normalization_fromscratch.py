# Normatizations
# https://en.wikipedia.org/wiki/Normalization_(statistics)

# Versions:
# 01 - Aug 11th, 2021 - Starter,
# 02 - May 21th, 2022 - Adjusting for Pandas options,
# 03 - May 21th, 2022 - Adding a dictionary with parameters,
# 04 - Jun 17th, 2023 - New features,
# 05 -

# Suggestions:
# - 


# Libraries
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


# Min-Max normalization function
def normalize_minmax(DataFrame, columns=None, verbose=False):
    """
    Returns the normalization by Min-Max strategy AND a dictionary
    with Minimum and Maximum for each normalization.
    
    """
    # Data preparation
    data = DataFrame.copy()
    params_norm = {}

    # Columns preparation
    if(columns == None):
        columns = data.columns.tolist()

    # Applying Min-Max
    for col in columns:
        data_min = data[col].min()
        data_max = data[col].max()

        data[col] = data[col].apply(lambda x: (x - data_min) / (data_max - data_min))

        params_norm[col] = {"method": "Min Max", "min": data_min, "max": data_max}


    return data, params_norm        

    
# Standard Score normalization function
def normalize_standscore(DataFrame, columns=None, verbose=False):
    """
    Returns the normalization by Standard Score strategy AND a
    dictionary with Mean and Standard Deviation for each normalization.
    
    """
    # Data preparation
    data = DataFrame.copy()
    params_norm = {}

    # Columns preparation
    if(columns == None):
        columns = data.columns.tolist()

    # Applying Standard Score
    for col in columns:
        data_mean = data[col].mean()
        data_stddev = data[col].std()

        data[col] = data[col].apply(lambda x: (x - data_mean) / data_stddev)

        params_norm[col] = {"method": "Standard Score", "mean": data_mean, "stddev": data_stddev}


    return data, params_norm       


def apply_normalization(DataFrame, params, verbose=True):
    """
    Applies the **params** to normalize the DataFrame.
    
    """
    data = DataFrame.copy()
    data_columns = data.columns.tolist()

    # Equation: Invert Trasformation

    # Invert Min Max transformation
    # xt = (x - min) / (max - min)
    # Isol x:
    # xt * (max - min) = (x - min)
    # x = (xt * (max - min)) + min

    # Invert Standard Score transformation
    # xt = (x - mean) / stddev
    # Isol x:
    # xt * stddev = x - mean
    # x = (xt * stddev) + mean


    for col in params.keys():
        if(data_columns.count(col) == True):
            method = params[col]["method"]

            if(method == "Min Max"):
                data_min = params[col]["min"]
                data_max = params[col]["max"]

                data[col] = data[col].apply(lambda xt: (xt * (data_max - data_min)) + data_min)
                

            elif(method == "Standard Score"):
                data_mean = params[col]["mean"]
                data_stddev = params[col]["stddev"]

                data[col] = data[col].apply(lambda xt: (xt * data_stddev) + data_mean)
                

            else:
                if(verbose == True):
                    print(f' >>> Error: method {method} not valid')
            

        else:
            if(verbose == True):
                print(f' > Warning: column {col} not found at DataFrame')


    return data


# end
