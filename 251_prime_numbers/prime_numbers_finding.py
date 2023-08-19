
# Libraries
import numpy as np
from prime_numbers_v01 import *


# Program ---------------------------------------------------------------

limit_list = [10, 100, 500, 1000, 2000, 5000, 10000, 20000]

for limit in limit_list:
    prime_number_list, time = prime_numbers(limit)
    print(f" > from 1 to {limit} has {len(prime_number_list)} prime numbers. [{time:.4f} s]")
    
