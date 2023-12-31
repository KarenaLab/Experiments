
# Libraries
import numpy as np
import scipy.stats as stats


# Functions
def z_confidence(mean, stddev, size, ci=0.95, seed=None, verbose=True):
    """

    More info:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html

    """
    # Seed
    if(seed != None and isinstance(seed, int) == True):
        np.random.seed(seed)
    
    # Synthetic data
    x = np.random.normal(loc=mean, scale=stddev, size=size)

    # Confidence interval sides
    step = (1 - ci) / 2
    left_tab = np.round(0 + step, decimals=6)
    right_tab = np.round(1 - step, decimals=6)

    # Statistics
    mean_hat = np.mean(x)
    stddev_hat = np.std(x)

    lower = mean_hat + (stats.norm.ppf(left_tab) * stddev_hat / np.sqrt(size))
    upper = mean_hat + (stats.norm.ppf(right_tab) * stddev_hat / np.sqrt(size))


    if(verbose == True):
        print(f" > mean:{mean_hat}, lower:{lower}, upper:{upper}")


    return mean_hat, lower, upper


def t_confidence(mean, stddev, size, ci=0.95, seed=None, verbose=True):
    """

    More info:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html

    """
    # Seed
    if(seed != None and isinstance(seed, int) == True):
        np.random.seed(seed)
    
    # Synthetic data
    x = np.random.normal(loc=mean, scale=stddev, size=size)

    # Confidence interval sides
    step = (1 - ci) / 2
    left_tab = np.round(0 + step, decimals=6)
    right_tab = np.round(1 - step, decimals=6)

    # Statistics
    mean_hat = np.mean(x)
    stddev_hat = np.std(x)

    lower = mean_hat + (stats.t.ppf(left_tab, df=(size - 1)) * stddev_hat / np.sqrt(size))
    upper = mean_hat + (stats.t.ppf(right_tab, df=(size - 1)) * stddev_hat / np.sqrt(size))


    if(verbose == True):
        print(f" > mean:{mean_hat}, lower:{lower}, upper:{upper}")


    return mean_hat, lower, upper

    

# end
