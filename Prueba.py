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


# Tablas de Hechos


orders = pd.read_csv('RAW/sales_order.csv')
items = pd.read_csv('RAW/sales_order_item.csv')
address = pd.read_csv('RAW/address.csv')
province = pd.read_csv('RAW/province.csv')


fact_ventas = items.merge(orders, on='order_id', how='left')


fact_ventas = fact_ventas.merge(address[['address_id', 'province_id']], 
                                left_on='shipping_address_id', 
                                right_on='address_id', 
                                how='left')


fact_ventas = fact_ventas.merge(province[['province_id', 'name']], 
                                on='province_id', 
                                how='left')


fact_ventas = fact_ventas[[
    'order_item_id',          
    'order_id',
    'order_date',
    'customer_id',
    'channel_id',
    'product_id',
    'province_id',
    'name',                   
    'quantity',
    'unit_price',
    'discount_amount',
    'line_total',
    'total_amount'
]]


fact_ventas.to_csv('DW/Fact_Ventas.csv', index=False)


sessions = pd.read_csv('RAW/web_session.csv')


sessions['date_id'] = pd.to_datetime(sessions['started_at']).dt.strftime('%Y%m%d').astype(int)


fact_actividad = sessions[['session_id', 'customer_id', 'date_id', 'source', 'device']]


fact_actividad.to_csv('DW/Fact_Actividad.csv', index=False)



nps = pd.read_csv('RAW/nps_response.csv')


nps['date_id'] = pd.to_datetime(nps['responded_at']).dt.strftime('%Y%m%d').astype(int)


nps['is_promoter'] = (nps['score'] >= 9).astype(int)
nps['is_detractor'] = (nps['score'] <= 6).astype(int)


fact_nps = nps[['nps_id', 'customer_id', 'channel_id', 'date_id', 'score', 'is_promoter', 'is_detractor']]

fact_nps.to_csv('DW/Fact_NPS.csv', index=False)



