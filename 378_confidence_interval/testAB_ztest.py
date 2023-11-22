
# Libraries
import numpy as np
import scipy.stats as stats
from statsmodels.stats.weightstats import ztest


# Functions
def two_side_ztest(sample, value=None):
    """
    Performs a two side z-test.

    if you wish to perform a null test under a different reference
    value, set **value**.

    """
    # Set the value as mean_zero for a shiffted null test.
    if(value == None):
        mean_zero = 0
    else:
        mean_zero = value

    # Stats
    mean_hat = np.mean(sample)
    stddev_hat = np.std(sample)

    z = (mean_hat - mean_zero) / (stddev_hat / np.sqrt(np.size(sample)))
    p_left = stats.norm.cdf(-1 * np.abs(z))
    p_right = 1 - stats.norm.cdf(np.abs(z))
    p = p_left + p_right

    return z, p


def one_side_ztest(sample):
    """
    Performs a one side z-test.

    """
    # Stats
    mean_hat = np.mean(sample)
    stddev_hat = np.std(sample)

    z = mean_hat / (stddev_hat / np.sqrt(np.size(sample)))
    p = 1 - stats.norm.cdf(z)

    return z, p


# Setup/Config
np.random.seed(137)


# Program --------------------------------------------------------------
n = 100
mean = 0.2
stddev = 1

x1 = np.random.normal(loc=mean, scale=stddev, size=n)

print("Two side z-test")
print(ztest(x1))
print(two_side_ztest(x1))
print("")

print("One side z-test")
print(ztest(x1, alternative="larger"))
print(one_side_ztest(x1))
print("")

print("Two side z-test under a different value")
print(ztest(x1, value=0.2))
print(two_side_ztest(x1, value=0.2))
print("")

# end
