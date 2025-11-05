import pandas as pd
import os

os.makedirs('DW', exist_ok=True)


store = pd.read_csv('RAW/store.csv')
address = pd.read_csv('RAW/address.csv')
province = pd.read_csv('RAW/province.csv')


dim_tienda = store.merge(address, on='address_id', how='left')


dim_tienda = dim_tienda.merge(
    province[['province_id', 'name', 'code']],
    on='province_id',
    how='left',
    suffixes=('', '_province')
)


dim_tienda = dim_tienda[[
    'store_id',
    'name',              
    'line1',
    'line2',
    'city',
    'province_id',
    'name_province',     
    'code',               
    'postal_code',
    'country_code',
    'created_at'
]]


dim_tienda.to_csv('DW/DimTienda.csv', index=False)

