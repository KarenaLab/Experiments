# PNS 2019 (IBGE) [P396]
# Demographic data from Brazil (data collection made in 2019.


# Libraries
import numpy as np
import pandas as pd


# Functions
def load_dataset():
    filename = "pns2019_bmi.csv"
    data = pd.read_csv(filename, sep=",", encoding="utf-8")

    return data


# Program ---------------------------------------------------------------      

df = load_dataset()

# Pivoting
all_stat = pd.DataFrame(data=[])        # Empty dataframe for storage

for state in df["state"].unique():
    data_state = df.groupby(by="state").get_group(state)

    for age_group in df["age_group"].unique():
        data_age = data_state.groupby(by="age_group").get_group(age_group)

        # Stats
        age_total = data_age.shape[0]

        line_stat = dict()              # Reset dictionary
        line_stat["state"] = state
        line_stat["age_group"] = age_group
        line_stat["total"] = age_total

        for bmi_class in data_age["bmi_class"].unique():
            data_bmi = data_age.groupby(by="bmi_class").get_group(bmi_class)
            line_stat[bmi_class] = np.round(((data_bmi.shape[0] / age_total) * 100), decimals=4)

        _values = pd.Series(line_stat)
        all_stat = pd.concat([all_stat, _values.to_frame().T], ignore_index=True)

            
# Organizing
all_stat = all_stat[["state", "age_group", "total", "underweight", "healthy", "overweight", "obesity_1", "obesity_2", "obesity_3"]]
all_stat = all_stat.fillna(value=0)

# Export
all_stat.to_csv("pns_bmi_percentuals.csv", index=False, sep=",", encoding="utf-8")


# end

        

