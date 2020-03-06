import pandas as pd
from pandas import read_csv
pd.options.display.width = 0
pd.options.display.max_rows = None
# pd.options.display.precision = 2

df = read_csv('susa2018.txt', header=0, sep=';')
print(df.info())
print(df.head())
