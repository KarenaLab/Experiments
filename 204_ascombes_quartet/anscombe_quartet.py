# Anconbe's Quartet [P204] ---------------------------------------------
# A group of four distinct set of values shows that only look for some
# metrics is not enough.
#
# https://en.wikipedia.org/wiki/Anscombe%27s_quartet


# Libraries
from collections import namedtuple

import numpy as np
import pandas as pd

from sklearn.metrics import r2_score

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Functions
def load_dataset():
    """
    Creates the Anscombe's dataset.

    """
    data1 = [[10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
             [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]]

    data2 = [[10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
             [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]]

    data3 = [[10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
             [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]]

    data4 = [[8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
             [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]]


    data1 = np.transpose(np.array(data1))
    data2 = np.transpose(np.array(data2))
    data3 = np.transpose(np.array(data3))
    data4 = np.transpose(np.array(data4))

    data1 = pd.DataFrame(data=data1, columns=["x", "y"])
    data2 = pd.DataFrame(data=data2, columns=["x", "y"])
    data3 = pd.DataFrame(data=data3, columns=["x", "y"])
    data4 = pd.DataFrame(data=data4, columns=["x", "y"])


    return data1, data2, data3, data4


def plot_anscombes(data1, data2, data3, data4):
    """
    Internal function for Anscombe's Quarte plot.

    """
    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.weight"] = 8
    plt.rcParams["xtick.bottom"] = False
    plt.rcParams["ytick.right"] = False
    
    # Figure
    fig = plt.figure(figsize=[8, 4.5])
    grd = gridspec.GridSpec(nrows=2, height_ratios=[1, 1], hspace=0.35,
                            ncols=2, width_ratios=[1, 1], wspace=0.30)

    title = "Anscombes Quartet"
    fig.suptitle(title, fontsize=10, weight="bold")

    ax0 = plt.subplot(grd[0, 0])                            # First Plot
    ax1 = plt.subplot(grd[0, 1], sharex=ax0, sharey=ax0)    # Second Plot
    ax2 = plt.subplot(grd[1, 0], sharex=ax1, sharey=ax1)    # Third Plot
    ax3 = plt.subplot(grd[1, 1], sharex=ax2, sharey=ax2)    # Fourth Plot

    # Plots
    ax0.scatter(data1["x"], data1["y"], color="darkblue", edgecolor="white", zorder=20)
    ax0.plot([2,20], [4,13], color="darkred", linewidth=1, zorder=21)

    ax1.scatter(data2["x"], data2["y"], color="darkblue", edgecolor="white", zorder=22)
    ax1.plot([2,20], [4,13], color="darkred", linewidth=1, zorder=23)

    ax2.scatter(data3["x"], data3["y"], color="darkblue", edgecolor="white", zorder=24)
    ax2.plot([2,20], [4,13], color="darkred", linewidth=1, zorder=25)

    ax3.scatter(data4["x"], data4["y"], color="darkblue", edgecolor="white", zorder=26)
    ax3.plot([2,20], [4,13], color="darkred", linewidth=1, zorder=27)


    ax0.set_xlim([2, 20])
    ax0.set_ylim([2, 14])

    ax0.set_xlabel("x1", fontsize=8)
    ax0.set_ylabel("y1", fontsize=8)
    ax0.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5)

    ax1.set_xlabel("x2", fontsize=8)
    ax1.set_ylabel("y2", fontsize=8)
    ax1.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5)

    ax2.set_xlabel("x3", fontsize=8)
    ax2.set_ylabel("y3", fontsize=8)
    ax2.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5)

    ax3.set_xlabel("x4", fontsize=8)
    ax3.set_ylabel("y4", fontsize=8)
    ax3.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5)

    #plt.savefig(title, dpi=240)
    plt.show()


    return None


def metrics(DataFrame, title=None):
    """
    Returns the metrics (measures) that Ascombe used to prove that
    a visualization is important.  

    """
    # Data preparation
    x = np.array(DataFrame["x"])
    y = np.array(DataFrame["y"])

    metr_tuple = namedtuple("metrics", ["x_mean", "y_mean", "x_var", "y_var", "a", "b", "corr", "r2"])

    # Title
    if(title != None):
        print(f"   ****  {title}  ****")

    # Metrics (from Ascombe)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_var = np.var(x)
    y_var = np.var(y)

    b, a = np.polyfit(x, y, deg=1)
    y_pred = [a + b * i for i in x]

    corr = np.corrcoef(x, y)[1, 0]
    r2 = r2_score(y, y_pred)

    # Print metrics
    print(f" >     Mean x: {x_mean:.3f}")
    print(f" >     Mean y: {y_mean:.3f}")
    print(f" > Variance x: {x_var:.3f}")
    print(f" > Variance y: {y_var:.3f}")
    print(f" >    Pearson: {corr:.3f}")
    print(f" >   Lin Regr: {a:.3f} + {b:.3f} * x")
    print(f" >  R Squared: {r2:.3f} \n")

    # Response
    metr = metr_tuple(x_mean, y_mean, x_var, y_var, a, b, corr, r2)


    return metr
    


# Program
data1, data2, data3, data4 = load_dataset()

plot_anscombes(data1, data2, data3, data4)

for index, data in enumerate([data1, data2, data3, data4], start=1):
    _ = metrics(data, title=f"Data {index}")


# end
