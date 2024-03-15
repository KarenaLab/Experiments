# Name [P414]
# Example to test the Standard Deviation of a play


# Libraries
import os
import sys
import itertools


import matplotlib.pyplot as plt


# Personal modules
sys.path.append(r"c:\python_modules")


# Functions
def k_dices(k=2):
    """


    """
    res = list(itertools.product(range(1, 7), repeat=k))

    return res


def dice_play(array):
    """


    """
    sum_dict = dict()
    for p in array:
        summation = sum([x for x in p])

        if summation in sum_dict.keys():
            sum_dict[summation] = sum_dict[summation] + 1

        else:
            sum_dict[summation] = 1


    return sum_dict
        

# Program --------------------------------------------------------------
for i in range(1, 6):
    print(dice_play(k_dices(k=i)))
    print("")
    

# end

