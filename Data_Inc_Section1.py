import numpy as np
import pandas as pd

file = "county_lex_2020-04-14.csv.gz"

df 	= pd.read_csv(file, compression='gzip', header=0)
countys = df.columns.values[1:]
col_names = dict(zip(countys, ["a" + lab for lab in countys]  ))
df 	= df.rename(columns = col_names)
df_long	= pd.wide_to_long(df, stubnames="a", i=['COUNTY_PRE'], j='col')
df_long = df_long.reset_index(drop=False)
df_long = df_long.rename(columns = {"col" : "COUNTY", "a" : "LEX"})
df_long.to_csv(r'reshaped.csv',index=False)