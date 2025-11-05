import pandas as pd
import os


os.makedirs('DW', exist_ok=True)


orders = pd.read_csv('RAW/sales_order.csv')
items = pd.read_csv('RAW/sales_order_item.csv')
address = pd.read_csv('RAW/address.csv')



Fact_sales_order_item = items.merge(orders, on='order_id', how='left', suffixes=["","_order"])


Fact_sales_order_item = Fact_sales_order_item.merge(
    address[['address_id', 'province_id']],
    left_on='shipping_address_id',
    right_on='address_id',
    how='left'
)




Fact_sales_order_item['date_id'] = pd.to_datetime(
    Fact_sales_order_item['order_date'], errors='coerce'
).dt.strftime('%Y%m%d').astype('Int64')




Fact_sales_order_item.to_csv('DW/fact_sales_order_item.csv', index=False)



