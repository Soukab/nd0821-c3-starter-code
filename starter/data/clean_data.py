import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')
df_clean = df.copy(deep=True)
df_clean.drop_duplicates(inplace=True)
df_clean.replace({'?': np.nan}, inplace = True)
df_clean.dropna(axis='columns', how='any', inplace=True)
df_clean.drop(" capital-gain", axis=1, inplace=True)
df_clean.drop(" capital-loss", axis=1, inplace=True)
new_name_columns = [x.strip(' ') for x in df_clean.columns]
df_clean.columns = new_name_columns
df_clean.to_csv('clean_census.csv')