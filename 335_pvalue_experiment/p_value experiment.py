
# Libraries
import numpy as np


# Functions
def rate_calc(conv_a, not_conv_a, conv_b, not_conv_b):
    """
    Returns the rate difference between conv_a and conv_b.
    Sample A need to be bigger than B.

    """
    rate_a = conv_a / (conv_a + not_conv_a)
    rate_b = conv_b / (conv_b + not_conv_b)

    diff = rate_a - rate_b

    return diff


def sample_shuffle(conv_a, not_conv_a, conv_b, not_conv_b):
    """
    Creates a bag and shuffle it.
    Returns tests rates (

    """
    # Generates the bag and shuffles it
    sample = np.zeros(conv_a + not_conv_a + conv_b + not_conv_b)
    sample[ :(conv_a + conv_b)] = 1
    np.random.shuffle(sample)

    # Separates the two bags
    bag_a = sample[ :(conv_a + not_conv_a)]
    bag_b = sample[-(conv_b + not_conv_b): ]

    # Counts the test rate and not rate for both bags.
    t_conv_a = (bag_a == 1).sum()
    t_not_conv_a = (bag_a == 0).sum()

    t_conv_b = (bag_b == 1).sum()
    t_not_conv_b = (bag_b == 0).sum()

    return t_conv_a, t_not_conv_a, t_conv_b, t_not_conv_b


# Setup/Config
np.random.seed(302)




# Program --------------------------------------------------------------
print("\n Practical Statistics for Data Scientists (Chap.03, page 95)\n")

# Results of sales test
conv_a, not_conv_a = 200, 23539
conv_b, not_conv_b = 182, 22406

# Test parameters
test = 20
repeat = 1000


# Sales conversion rate from experiment
rate_diff = rate_calc(conv_a, not_conv_a, conv_b, not_conv_b)

pvalue_list = np.array([])
for i in range(1, test+1):

    diff_list = np.array([])
    for j in range(0, repeat):
        test_conv_a, test_not_conv_a, test_conv_b, test_not_conv_b = sample_shuffle(conv_a, not_conv_a, conv_b, not_conv_b)
        test_rate_diff = rate_calc(test_conv_a, test_not_conv_a, test_conv_b, test_not_conv_b)
        diff_list = np.append(diff_list, test_rate_diff)


    p_value = ((diff_list > rate_diff).sum() / repeat) * 100
    pvalue_list = np.append(pvalue_list, p_value)
    print(f" > Test {i}: p-value = {p_value:.1f}")


# end
