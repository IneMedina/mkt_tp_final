import pandas as pd
import os


province = pd.read_csv('RAW/province.csv')

dim_ubicacion = province.copy()

dim_ubicacion.to_csv('DW/DimUbicacion.csv', index=False)
