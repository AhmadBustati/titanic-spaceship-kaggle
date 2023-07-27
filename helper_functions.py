import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

def get_value_counts_and_missing(df, column_name,num_results ):
    """
    This function returns the unique values if it's less the  a specific number `num_results`
    and the number of missing value for non numeric column in a data frame  
    """
    num_unique= len(df[column_name].unique())
    num_missing = df[column_name].isna().sum()
    if num_unique>num_results:
        return num_unique,num_missing
    
    value_counts = df[column_name].value_counts() 

    return value_counts,num_missing
