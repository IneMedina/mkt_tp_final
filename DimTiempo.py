import pandas as pd
import os



dates = pd.date_range(start='2023-01-01', end='2023-12-31')

dim_tiempo = pd.DataFrame({
    'date': dates,
    'date_id': dates.strftime('%Y%m%d').astype(int),
    'month': dates.month,
    'year': dates.year
})

dim_tiempo.to_csv('DW/DimTiempo.csv', index=False)
