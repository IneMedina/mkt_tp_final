import pandas as pd
import os



channel = pd.read_csv('RAW/channel.csv')

dim_canal = channel.copy()

dim_canal.to_csv('DW/DimCanal.csv', index=False)
