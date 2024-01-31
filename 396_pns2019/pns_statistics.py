# PNS 2019 (IBGE) [P396]
# Demographic data from Brazil (data collection made in 2019.


# Libraries
import numpy as np
import pandas as pd


# Functions
def load_dataset():
    """
    Reads pns2019_bmi.csv file.
    Data from PNS 2019 with weight and height from Brazilian
    population.

    """
    filename = "pns2019_bmi.csv"
    data = pd.read_csv(filename, sep=",", encoding="utf-8")

    return data


def data_pivot(DataFrame, first_level, second_level, variable):
    """
    Pivots data with **first_level**, **second_level** beyond the
    **variable**.

    """
    data = DataFrame.copy()

    # New dataset to store info
    all_stat = pd.DataFrame(data=[])

    # First level
    for first in data[first_level].unique():
        data_first = data.groupby(by=first_level).get_group(first)

        # Second level
        for second in data_first[second_level].unique():
            data_second = data_first.groupby(by=second_level).get_group(second)
            level_total = data_second.shape[0]

            line_stat = dict()      # Reset dictionary
            line_stat[first_level] = first
            line_stat[second_level] = second
            line_stat["total"] = level_total

            # Variable
            for var in data_second[variable].unique():
                data_var = data_second.groupby(by=variable).get_group(var)
                line_stat[var] = np.round((data_var.shape[0] / level_total) * 100, decimals=5)


            # Store stats
            _values = pd.Series(line_stat)
            all_stat = pd.concat([all_stat, _values.to_frame().T], ignore_index=True)


    # Organize data
    all_stat = all_stat[["state", "age_group", "total", "underweight", "healthy", "overweight", "obesity_1", "obesity_2", "obesity_3"]]
    all_stat = all_stat.fillna(value=0)


    return all_stat
            
                


# Program ---------------------------------------------------------------      

df = load_dataset()
df_stat = data_pivot(df, first_level="state", second_level="age_group", variable="bmi_class")

  

