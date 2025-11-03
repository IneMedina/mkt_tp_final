import pandas as pd
import os

os.makedirs('DW', exist_ok=True)

orders = pd.read_csv('RAW/sales_order.csv')
items = pd.read_csv('RAW/sales_order_item.csv')
address = pd.read_csv('RAW/address.csv')
province = pd.read_csv('RAW/province.csv')


fact_ventas = items.merge(orders, on='order_id', how='left')


fact_ventas = fact_ventas.merge(
    address[['address_id', 'province_id']],
    left_on='shipping_address_id',
    right_on='address_id',
    how='left'
)

fact_ventas = fact_ventas.merge(
    province[['province_id', 'name']],
    on='province_id',
    how='left'
)


fact_ventas['date_id'] = pd.to_datetime(fact_ventas['order_date'], errors='coerce') \
                           .dt.strftime('%Y%m%d') \
                           .astype('Int64')


fact_ventas = fact_ventas[[
    'order_item_id',          
    'order_id',
    'date_id',              
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

