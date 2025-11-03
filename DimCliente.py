import pandas as pd
import os



customer = pd.read_csv('RAW/customer.csv')

dim_cliente = customer.copy()


dim_cliente.to_csv('DW/DimCliente.csv', index=False)

