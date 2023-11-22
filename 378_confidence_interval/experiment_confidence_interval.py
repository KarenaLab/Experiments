
# Libraries
import numpy as np
import scipy.stats as stats

from testAB_confidence_interval import *


# Setup/Config


# Program --------------------------------------------------------------

n = 100
mean = 5
stddev = 2

mean, lower, upper = z_confidence(mean, stddev, n, seed=137)
mean, lower, upper = t_confidence(mean, stddev, n, seed=137)
