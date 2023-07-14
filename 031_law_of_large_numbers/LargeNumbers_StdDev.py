# Versions --------------------------------------------------------------

# 01 - 19th Jan 2021 - Starter


# Libraries -------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# MAIN Program ----------------------------------------------------------

# Header

print("")
print(" *** LLN - Law of Large Numbers (Standard Deviation) ***")
print("")

# Variables

Sample= [10, 250, 1000, 5000]

Higher = max(Sample)
Step = Higher/20


i = 0
Sum = 0
Dice_List = []
Read_List = []
Mean_List = []
Lower_List = []
Upper_List = []
Axis_List = []


# Program

while(i < Higher):

    Dice = np.random.randint(low= 1, high= 7, size= 1)

    Dice_List.append(Dice)    
    Mean = np.mean(Dice_List)
    Mean = np.around(Mean, decimals= 4)
    
    Read_List.append(Mean)


    i = i+1

    if((i%10) == 0):

        # Mean was calculed in the last loop, don't need to be updated
        StdDev = np.std(Read_List)

        Upper = np.around(Mean + 3*StdDev, decimals= 4)
        Lower = np.around(Mean - 3*StdDev, decimals= 4)
        
        Axis_List.append(i)
        Mean_List.append(Mean)
        Upper_List.append(Upper)
        Lower_List.append(Lower)



# 2 - Plotting ---------------------------------------------------------

Title = f"Deviation of Law of Large Numbers ({Higher})"

fig = plt.figure(figsize= (8, 6))

fig.suptitle(Title, fontsize= 16)

plt.plot(Axis_List, Mean_List,
         color= "royalblue", linestyle= "-", linewidth= 1)

plt.plot(Axis_List, Upper_List,
         color= "lightsteelblue", linestyle= "-", linewidth= 0.5)

plt.plot(Axis_List, Lower_List,
         color= "lightsteelblue", linestyle= "-", linewidth= 0.5)

plt.fill_between(x= Axis_List, y1= Upper_List, y2= Lower_List,
                 color= "lightsteelblue", alpha= 0.5)

plt.axhline(y= 3.5,
            color= "darkred", linestyle= "-", linewidth= 0.5)


plt.tight_layout()
plt.savefig(Title, dpi= 240)
plt.show()




# Sources ---------------------------------------------------------------

# Random Functions = https://numpy.org/doc/1.16/reference/routines.random.html
# randint = https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html?highlight=randint#numpy.random.randint

# LLN Wikipedia (Law of Large Numbers) = https://en.wikipedia.org/wiki/Law_of_large_numbers
# LLN Wolfram (Law of Large Numbers) = https://mathworld.wolfram.com/WeakLawofLargeNumbers.html
