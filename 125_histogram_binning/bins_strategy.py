
# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# Versions -------------------------------------------------------------
# 01 - Jun 07th, 2023 - Starter
# 02 -


# Insights -------------------------------------------------------------
#


# Function -------------------------------------------------------------
def bins_strategy(Series, title=None, savefig=False, verbose=True):
    """
    Plots/shows the bins number for each binning strategy.
    Using numpy.histogram_bin_edges function.

    """
    label = Series.name
    
    data = np.array(Series)
    data = data[~(np.isnan(data))]

    bins_calc = []
    strategy_list = ["sqrt", "fd", "doane", "scott", "stone", "rice", "sturges"]

    for strategy in strategy_list:
        bins_edge = np.histogram_bin_edges(data, bins=strategy)
        no_bins = bins_edge.size
                
        bins_calc.append(no_bins)


    # Plot
    fig = plt.figure(figsize=[8, 4.5])

    # RC Params
    plt.rcParams["xtick.bottom"] = False
    plt.rcParams["ytick.direction"] = "inout"
    

    if(title == None):
        title = f"Binning Strategies - {label}"

    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.bar(x=strategy_list, height=bins_calc, color="navy", zorder=20)

    plt.ylabel("number of bins", loc="top")
    
    plt.grid(axis="y", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)

        if (verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()

    plt.close(fig)

    return None

# end
