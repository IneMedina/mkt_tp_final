import pandas as pd
import os


os.makedirs('DW', exist_ok=True)


orders = pd.read_csv('RAW/sales_order.csv')
address = pd.read_csv('RAW/address.csv')



Fact_sales_order = orders.merge(
    address[['address_id', 'province_id']],
    left_on='shipping_address_id',
    right_on='address_id',
    how='left'
)



Fact_sales_order['date_id'] = pd.to_datetime(
    Fact_sales_order['order_date'], errors='coerce'
).dt.strftime('%Y%m%d').astype('Int64')




Fact_sales_order.to_csv('DW/fact_sales_order.csv', index=False)


