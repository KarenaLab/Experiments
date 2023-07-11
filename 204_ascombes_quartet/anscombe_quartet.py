
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Data
# https://en.wikipedia.org/wiki/Anscombe%27s_quartet#

data = [["I_x", "I_y", "II_x", "II_y", "III_x", "III_y", "IV_x", "IV_y"],
        [10.0, 8.04, 10.0, 9.14, 10.0, 7.46, 8.0, 6.58],
        [8.0, 6.95, 8.0, 8.14, 8.0, 6.77, 8.0, 5.76],
        [13.0, 7.58, 13.0, 8.74, 13.0, 12.74, 8.0, 7.71],
        [9.0, 8.81, 9.0, 8.77, 9.0, 7.11, 8.0, 8.84],
        [11.0, 8.33, 11.0, 9.26, 11.0, 7.81, 8.0, 8.47],
        [14.0, 9.96, 14.0, 8.10, 14.0, 8.84, 8.0, 7.04],
        [6.0, 7.24, 6.0, 6.13, 6.0, 6.08, 8.0, 5.25],
        [4.0, 4.26, 4.0, 3.10, 4.0, 5.39, 19.0, 12.50],
        [12.0, 10.84, 12.0, 9.13, 12.0, 8.15, 8.0, 5.56],
        [7.0, 4.82, 7.0, 7.26, 7.0, 6.42, 8.0, 7.91],
        [5.0, 5.68, 5.0, 4.74, 5.0, 5.73, 8.0, 6.89]]

DF = pd.DataFrame(data=data[1: ], columns=data[0])


# Ploting
fig = plt.figure(figsize=[8, 4.5])

plt.rcParams["font.family"] = "Helvetica"
plt.rcParams["font.weight"] = 8
plt.rcParams["xtick.bottom"] = False
plt.rcParams["ytick.right"] = False


grd = gridspec.GridSpec(nrows=2, height_ratios=[1, 1], hspace=0.35,
                        ncols=2, width_ratios=[1, 1], wspace=0.30)

title = "Anscombes Quartet"
fig.suptitle(title, fontsize=10, weight="bold")

ax0 = plt.subplot(grd[0, 0])                            # First Plot
ax1 = plt.subplot(grd[0, 1], sharex=ax0, sharey=ax0)    # Second Plot
ax2 = plt.subplot(grd[1, 0], sharex=ax1, sharey=ax1)    # Third Plot
ax3 = plt.subplot(grd[1, 1], sharex=ax2, sharey=ax2)    # Fourth Plot

ax0.scatter(DF["I_x"], DF["I_y"], color="darkblue", edgecolor="white", zorder=20)
ax0.plot([2,20], [4,13], color="darkred", linewidth=1, zorder=21)

ax1.scatter(DF["II_x"], DF["II_y"], color="darkblue", edgecolor="white", zorder=22)
ax1.plot([2,20], [4,13], color="darkred", linewidth=1, zorder=23)

ax2.scatter(DF["III_x"], DF["III_y"], color="darkblue", edgecolor="white", zorder=24)
ax2.plot([2,20], [4,13], color="darkred", linewidth=1, zorder=25)

ax3.scatter(DF["IV_x"], DF["IV_y"], color="darkblue", edgecolor="white", zorder=26)
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

plt.savefig(title, dpi=240)
plt.show()
