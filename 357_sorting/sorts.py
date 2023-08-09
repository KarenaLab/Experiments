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
def sort_argmin(array):
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
    Do not laugh, I did this sorting algorithm in my APS Advanced Test
    because I need to sort a list and do not remember any algorithm.

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

        print(data)
        
        _ = input()


    return data

    

        
        




