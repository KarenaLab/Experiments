
# Libraries
import numpy as np
from prime_numbers_v01 import *


# Program ---------------------------------------------------------------

limit = 10000
rounds = 10
repeat = 5

print(f" > Doing {rounds} rounds of {repeat} repeated times")
print(f" > the calculation of prime numbers up to {limit}. \n")

time_process_list = []
process_mean, process_stddev = [], []

for i in range(0, rounds):
    for j in range(1, repeat+1):
        _, time_process = prime_numbers(limit)
        time_process_list.append(time_process)
        

    time_mean = np.mean(time_process_list)
    process_mean.append(time_mean)
    time_stddev = np.std(time_process_list)
    process_stddev.append(time_stddev)

    print(f" > Time to process: {time_mean:.2f} +/- {(3*time_stddev):.3f}s [{time_mean-(3*time_stddev):.3f}, {time_mean+(3*time_stddev):.3f}]s") 
