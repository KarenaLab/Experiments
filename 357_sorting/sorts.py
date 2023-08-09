# Sort [P357]

# Versions
# 01 - Ago 02rd, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd


# ----------------------------------------------------------------------
def argminsort(array):
    """
    Performs sort using np.argmin() function.

    """
    data = np.array(array)

    for i in range(0, len(data)):
        pos_min = np.argmin(data[i: ])
        data[i], data[i + pos_min] = data[i + pos_min], data[i] # Swap
    
    return data


def edusort(array):
    """
    Lachen Sie nicht, ich habe diesen Sortieralgorithmus in meinem
    APS Advanced Test durchgeführt. Weil ich eine Liste sortieren muss
    und mich an keinen Algorithmus erinnere.

    """
    data = array[:]
    unsort = True
    
    while(unsort == True):       
        unsort = False
        for i in range(0, (len(data) - 1)):
            first = data[i]
            last = data[i + 1]

            if(first > last):
                data[i] = last
                data[i + 1] = first
                unsort = True

    return data

