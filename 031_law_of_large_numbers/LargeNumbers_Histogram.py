
# Versions --------------------------------------------------------------

# 01 - 17th Jan 2021 - Starter



# Libraries 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



# MAIN Program ----------------------------------------------------------
print("")
print(" *** LLN - Law of Large Numbers (Four Lines) ***")
print("")

Round = 100
Bins = 11

Sample= [10, 250, 1000, 5000]
Higher = max(Sample)

Read_A = []
Read_B = []
Read_C = []
Read_D = []


r = 0

while(r < Round):

    i = 0
    Sum = 0
    Mean_List = []

    while(i < Higher):

        Dice = np.random.randint(low= 1, high= 7, size= 1)
        Sum = Sum + Dice
        Mean = np.around(Sum/(i+1), decimals= 4)
        Mean_List.append(Mean[0])

        i = i+1


    Read_A.append(Mean_List[Sample[0]-1])
    Read_B.append(Mean_List[Sample[1]-1])
    Read_C.append(Mean_List[Sample[2]-1])
    Read_D.append(Mean_List[Sample[3]-1])

    r = r+1
 


# 2 - Plotting ----------------------------------------------------------

Title = f"Histogram of Law of Large Numbers ({Higher})"

fig = plt.figure(figsize= (8, 6))
gs = gridspec.GridSpec(nrows= 1, ncols= 4, width_ratios= [1, 1, 1, 1])

fig.suptitle(Title, fontsize= 16)

ax0 = plt.subplot(gs[0])
ax0.hist(x= Read_A, bins= Bins)

Title = f"S= {Sample[0]} items"
ax0.set_title(Title, fontsize= 10)
ax0.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
ax0.set_axisbelow(True)
ax0.axvline(x= 3.5, color="yellow", linewidth= 0.75)


ax1 = plt.subplot(gs[1])
ax1.hist(x= Read_B, bins= Bins)

Title = f"S= {Sample[1]} items"
ax1.set_title(Title, fontsize= 10)
ax1.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
ax1.set_axisbelow(True)
ax1.axvline(x= 3.5, color="yellow", linewidth= 0.75)


ax2 = plt.subplot(gs[2])
ax2.hist(x= Read_C, bins= Bins)

Title = f"S= {Sample[2]} items"
ax2.set_title(Title, fontsize= 10)
ax2.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
ax2.set_axisbelow(True)
ax2.axvline(x= 3.5, color="yellow", linewidth= 0.75)


ax3 = plt.subplot(gs[3])
ax3.hist(x= Read_D, bins= Bins)

Title = f"S= {Sample[3]} items"
ax3.set_title(Title, fontsize= 10)
ax3.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
ax3.set_axisbelow(True)
ax3.axvline(x= 3.5, color="yellow", linewidth= 0.75)


plt.tight_layout()
plt.savefig(Title, dpi= 240)
plt.show()


# Sources ---------------------------------------------------------------

# Random Functions = https://numpy.org/doc/1.16/reference/routines.random.html
# randint = https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html?highlight=randint#numpy.random.randint

# LLN Wikipedia (Law of Large Numbers) = https://en.wikipedia.org/wiki/Law_of_large_numbers
# LLN Wolfram (Law of Large Numbers) = https://mathworld.wolfram.com/WeakLawofLargeNumbers.html
