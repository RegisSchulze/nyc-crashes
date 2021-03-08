import pandas as pd
import numpy as np
filename="/home/regis/Desktop/machine learning/ANT-Theano-2-27-main (1) (1)/ANT-Theano-2-27-main/additional_resources/datasets/NYC Motor Vehicle Crashes/data_100000.csv"
df = pd.read_csv(filename)
print(df.head())
nan_values = df.isnull().sum()
print(nan_values)
print(df.dtypes)
#we should at have at least a value for either on_street_name, off_street_name, cross_street_name
#the number columns have 0 nan-values and are all type int64
#contributing_factor_vehicle an accident should have at least one car
#drop rows that have  nan values for on_street_name, off_street_name, cross_street_neme
for col in df:
    print(col)
    print(df[col].unique())