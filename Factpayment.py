import pandas as pd
import os


os.makedirs('DW', exist_ok=True)


orders = pd.read_csv('RAW/sales_order.csv')
payments = pd.read_csv('RAW/payment.csv')
address = pd.read_csv('RAW/address.csv')



fact_payment = payments.merge(orders, on='order_id', how='left', suffixes=["","_order"])


fact_payment = fact_payment.merge(
    address[['address_id', 'province_id']],
    left_on='shipping_address_id',
    right_on='address_id',
    how='left'
)




fact_payment['date_id'] = pd.to_datetime(
    fact_payment['order_date'], errors='coerce'
).dt.strftime('%Y%m%d').astype('Int64')

fact_payment['paid_at_id'] = pd.to_datetime(
    fact_payment['paid_at'], errors='coerce'
).dt.strftime('%Y%m%d').astype('Int64')




fact_payment.to_csv('DW/Fact_payment.csv', index=False)



