import pandas as pd
import os


os.makedirs('DW', exist_ok=True)

# Dimenciones

customer = pd.read_csv('RAW/customer.csv')

dim_cliente = customer.copy()


dim_cliente.to_csv('DW/DimCliente.csv', index=False)


product = pd.read_csv('RAW/product.csv')

dim_producto = product.copy()

dim_producto.to_csv('DW/DimProducto.csv', index=False)


channel = pd.read_csv('RAW/channel.csv')

dim_canal = channel.copy()

dim_canal.to_csv('DW/DimCanal.csv', index=False)


province = pd.read_csv('RAW/province.csv')

dim_ubicacion = province.copy()

dim_ubicacion.to_csv('DW/DimUbicacion.csv', index=False)


dates = pd.date_range(start='2023-01-01', end='2023-12-31')

dim_tiempo = pd.DataFrame({
    'date': dates,
    'date_id': dates.strftime('%Y%m%d').astype(int),
    'month': dates.month,
    'year': dates.year
})

dim_tiempo.to_csv('DW/DimTiempo.csv', index=False)

