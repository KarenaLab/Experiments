# [P449] Pratical Time Series Analysis Exercise
# Exercise related to Brazilian Portuguese Book, page 039.


# Libraries
import os

import time
import datetime

import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt


# Personal modules
from smoothing_techniques import *


# Functions
def load_dataset():
    """
    Load dataset from US Bureau od Labor Statistics and convert it into
    an usable DataFrame. Series title: (Seas) Unemployment Rate
    
    More info: https://data.bls.gov/pdq/SurveyOutputServlet
    
    """
    filename = "US_Labor_SeriesReport-20241221195829_e8e89b.xlsx"

    # Load Dataset (Years as rows, Months as columns)
    data = pd.read_excel(filename, index_col=0)

    # Convert into a Timestamp DataFrame
    data_ts = pd.DataFrame(data=[])

    for year in data.index:                 # Source rows
        for month in data.columns:          # Source columns
            date = convert_timestamp(year, month)
            date = datetime.datetime.strptime(date, "%Y-%m-%d")

            data_ts.loc[date, "unemployment_rate"] = data.loc[year, month]
            
            
    return data_ts


def convert_timestamp(year, month):
    month = month_number(month, output="string")
    string = f"{year}-{month}-01"

    return string
    
    
def month_number(string, output="numeric"):
    """
    Receives month as a 03 letters string and returns the numeric value
    of (Output could be numeric (default) or 02 digits string.

    """
    month_dict = {"Jan": "01", "Feb": "02", "Mar": "03",
                  "Apr": "04", "May": "05", "Jun": "06",
                  "Jul": "07", "Aug": "08", "Sep": "09",
                  "Oct": "10", "Nov": "11", "Dec": "12"}

    if(list(month_dict.keys()).count(string) == 1):
        answer = month_dict[string]

        if(output == "numeric"):
            answer = int(answer)
        
    else:
        answer = None   # Not a good practice


    return answer


# Program --------------------------------------------------------------
df = load_dataset()

df["unemployment_rate"] = moving_average(df["unemployment_rate"], window=3)

# end

