# PNS 2019 (IBGE) [P396]
# Demographic data from Brazil (data collection made in 2019.


# Libraries
import numpy as np
import pandas as pd


# Functions
def read_txt(filename):
    file = open(filename, mode="r")
    lines = file.readlines()

    file.close()

    return lines


def _load_states(text):
    value = text[0:2].strip(" ")

    if(value != ""):
        br_states= {11: ["RO", "Roraima", "Norte"],
                    12: ["AC", "Acre", "Norte"],
                    13: ["AM", "Amazonas", "Norte"],
                    14: ["RR", "Roraima", "Norte"],
                    15: ["PA", "Para", "Norte"],
                    16: ["AP", "Amapa", "Norte"],
                    17: ["TO", "Tocantins", "Norte"],
                    21: ["MA", "Maranhao", "Nordeste"],
                    22: ["PI", "Piaui", "Nordeste"],
                    23: ["CE", "Ceara", "Nordeste"],
                    24: ["RN", "Rio Grande do Norte", "Nordeste"],
                    25: ["PB", "Paraiba", "Nordeste"],
                    26: ["PE", "Pernambuco", "Nordeste"],
                    27: ["AL", "Alagoas", "Nordeste"],
                    28: ["SE", "Sergipe", "Nordeste"],
                    29: ["BA", "Bahia", "Nordeste"],
                    31: ["MG", "Minas Gerais", "Sudeste"],
                    32: ["ES", "Espirito Santo", "Sudeste"],
                    33: ["RJ", "Rio de Janeiro", "Sudeste"],
                    35: ["SP", "Sao Paulo", "Sudeste"],
                    41: ["PR", "Parana", "Sul"],
                    42: ["RS", "Rio Grande do Sul", "Sul"],
                    43: ["SC", "Santa Catarina", "Sul"],
                    50: ["MS", "Mato Grosso do Sul", "Centro_Oeste"],
                    51: ["MT", "Mato Grosso", "Centro_Oeste"],
                    52: ["GO", "Goias", "Centro_Oeste"],
                    53: ["DF", "Distrito Federal", "Centro_Oeste"]}

        value = br_states[int(value)][0]

    return value


def _load_age(text):
    value = text[116:119].strip(" ")

    if(value != ""):
        value = int(value)

    return value


def _load_gender(text):
    value = text[108].strip(" ")

    if(value != ""):
        if(value == "1"):
            value = "male"

        elif(value == "2"):
            value = "female"

        elif(value == "3"):
            value = "not answer"

        else:
            value = ""

    return value


def _load_weight(text):
    value = text[606:609].strip(" ")

    if(value != ""):
        value = int(value)

    return value


def _load_height(text):
    value = text[616:619].strip(" ")

    if(value != ""):
        value = int(value)

    return value


def bmi_classification(value):
    if(value < 18.5):
        bmi_class = "underweight"

    elif(value >= 18.5 and value < 25):
        bmi_class = "healthy"

    elif(value >= 25 and value < 30):
        bmi_class = "overweight"

    elif(value >= 30 and value < 35):
        bmi_class = "obesity_1"

    elif(value >= 35 and value < 40):
        bmi_class = "obesity_2"

    elif(value >= 40):
        bmi_class = "obesity_3"

    else:
        bmi_class = np.nan

    return bmi_class


def agegroup_classification(value):
    if(value < 20):
        age_group = "under_20"

    elif(value >= 20 and value < 30):
        age_group = "20_to_29"

    elif(value >= 30 and value < 40):
        age_group = "30_to_39"

    elif(value >= 40 and value < 50):
        age_group = "40_to_49"

    elif(value >= 50 and value < 60):
        age_group = "50_to_59"

    elif(value >= 60 and value < 70):
        age_group = "60_to_69"
    
    elif(value >= 70 and value < 80):
        age_group = "70_to_79"

    elif(value >= 80 and value < 90):
        age_group = "80_to_89"

    elif(value >= 90):
        age_group = "over 90"

    else:
        age_group= np.nan

    return age_group


def extract_data(text, export=False):
    # User stats
    data_empty = 0
    data_bmi = 0

    # Data storage
    bmi_list = list()

    for t in text:
        state = _load_states(t)
        age = _load_age(t)
        gender = _load_gender(t)

        weight = _load_weight(t)
        height = _load_height(t)

        if(isinstance(weight, int) == True and isinstance(height, int) == True):
            data_bmi = data_bmi + 1
            bmi_list.append([state, age, gender, height, weight])

        else:
            data_empty = data_empty + 1


    # Create dataset
    df = pd.DataFrame(data=bmi_list, columns=["state", "age", "gender", "height_cm", "weight_kg"])
    df["bmi"] = np.round(df["weight_kg"] / ((df["height_cm"] / 100) ** 2), decimals=4)
    df["bmi_class"] = df["bmi"].apply(lambda x: bmi_classification(x))
    df["age_group"] = df["age"].apply(lambda x: agegroup_classification(x))

    # Export data
    if(export == True):
        df.to_csv("pns2019_bmi.csv", index=False, sep=",", encoding="utf-8")
        

    return df, data_bmi, data_empty

# Program ---------------------------------------------------------------

# Extract data from raw .txt file and export
filename = "PNS_2019.txt"
df_pns, data_bmi, data_empty = extract_data(read_txt(filename), export=True)

        


