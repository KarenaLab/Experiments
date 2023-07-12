

# Versions --------------------------------------------------------------

# 01 - 17th Jan 2021 - Starter
# 02 - 17th Jan 2021 - Lists with various Samples



# Libraries -------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt



# Setup -----------------------------------------------------------------

# Sample for Test (Change Coments for test)

List100 = [10, 25, 50, 100]
List200 = [10, 50, 100, 200]
List500 = [10, 100, 250, 500]
List1000 = [10, 100, 500, 1000]
List5000 = [10, 250, 1000, 5000]
List10000 = [10, 1000, 5000, 10000]



# MAIN Program ----------------------------------------------------------

# 0 - Header ------------------------------------------------------------

print("")
print(" *** LLN - Law of Large Numbers (Lei dos Grandes Números) ***")
print("")


Sample = List5000


# 1 - Calculating Moving Mean -------------------------------------------

Sum = 0
Mean = 0
Mean_List = []

Higher = max(Sample)
Axis_X = np.linspace(start= 1, stop= Higher, num= Higher)

i = 0
step = 0

while(step < len(Sample)):

    while(i < Sample[step]):

        Dice = np.random.randint(low= 1, high= 7, size= 1)
        Sum = Sum + Dice
        Mean = np.around(Sum/(i+1), decimals= 4)
        Mean_List.append(Mean[0])
        
        i = i+1

    Error = np.around((abs(Mean - 3.5)/3.5)*100, decimals= 2)
    print(f"Mean({i}): {Mean}  >>>  Error: {Error[0]}%")

    step = step+1

print("")   


# 2 - Plotting ----------------------------------------------------------

Title = f"Testing Law of Large Numbers with One Dice ({Higher})"

fig = plt.figure(figsize= (8, 6))
ax = fig.add_subplot(1, 1, 1)

ax.plot(Axis_X, Mean_List, color= "blue", label= "Mean")

ax.set_title(Title, fontsize= 16)
ax.set_xlabel("No. Samples")

ax.set_ylabel("Dice")
ax.set_ylim(bottom= 0.5, top= 6.5)

ax.grid(color= "grey", linestyle= "--", linewidth= 0.5)
ax.set_axisbelow(True)

plt.axhline(y= 3.5, color= "red", linewidth= 1, label= "LLN Mean")


offset = int(Higher/100)

for i in Sample:

    Axis = i
    Label = str(i)
    Text = f"Mean = {Mean_List[i-1]}"
    
    plt.axvline(x= Axis, color= "black", linewidth= 0.75)
    plt.text(x= (Axis+offset), y= 1.2, s= Label, rotation= 90, alpha= 1)
    plt.text(x= (Axis+offset), y= 4.5, s= Text, rotation= 90, alpha= 1)

    
plt.tight_layout()
plt.savefig(Title, dpi= 240)
plt.show()



# Sources ---------------------------------------------------------------

# Random Functions = https://numpy.org/doc/1.16/reference/routines.random.html
# randint = https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html?highlight=randint#numpy.random.randint

# LLN Wikipedia (Law of Large Numbers) = https://en.wikipedia.org/wiki/Law_of_large_numbers
# LLN Wolfram (Law of Large Numbers) = https://mathworld.wolfram.com/WeakLawofLargeNumbers.html

