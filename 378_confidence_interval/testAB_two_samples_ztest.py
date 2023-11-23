
# Libraries
import numpy as np
import scipy.stats as stats
from statsmodels.stats.weightstats import ztest


# Functions
def two_sample_ztest(sample_1, sample_2):
    """
    Performs...

    """
    # Stats
    mean_1_hat = np.mean(sample_1)
    mean_2_hat = np.mean(sample_2)
    diff_mean_hat = mean_1_hat - mean_2_hat

    var_1_hat = np.var(sample_1)
    var_2_hat = np.var(sample_2)
    stddev_hat = np.sqrt((var_1_hat / np.size(sample_1)) + (var_2_hat / np.size(sample_2)))

    z = diff_mean_hat / stddev_hat
    p_left = stats.norm.cdf(-1 * np.abs(z))
    p_right = 1 - stats.norm.cdf(np.abs(z))
    p = p_left + p_right

    return z, p


# Setup/Config
np.random.seed(137)


# Program --------------------------------------------------------------
n_0 = 100
mean_0 = 0.2
stddev_0 = 1
x0 = np.random.normal(loc=mean_0, scale=stddev_0, size=n_0)

n_1 = 100
mean_1 = 0.5
stddev_1= 1
x1 = np.random.normal(loc=mean_1, scale=stddev_1, size=n_1)


print(ztest(x0, x1))
print(two_sample_ztest(x0, x1))
print("")


