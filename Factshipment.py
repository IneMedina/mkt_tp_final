import pandas as pd
import os


os.makedirs('DW', exist_ok=True)


orders = pd.read_csv('RAW/sales_order.csv')
shipments = pd.read_csv('RAW/shipment.csv')
address = pd.read_csv('RAW/address.csv')



fact_shipment = shipments.merge(orders, on='order_id', how='left', suffixes=["","_order"])


fact_shipment = fact_shipment.merge(
    address[['address_id', 'province_id']],
    left_on='shipping_address_id',
    right_on='address_id',
    how='left'
)




fact_shipment['date_id'] = pd.to_datetime(
    fact_shipment['order_date'], errors='coerce'
).dt.strftime('%Y%m%d').astype('Int64')

fact_shipment['shipped_at_id'] = pd.to_datetime(
    fact_shipment['shipped_at'], errors='coerce'
).dt.strftime('%Y%m%d').astype('Int64')

fact_shipment['delivered_at_id'] = pd.to_datetime(
    fact_shipment['delivered_at'], errors='coerce'
).dt.strftime('%Y%m%d').astype('Int64')




fact_shipment.to_csv('DW/Fact_shipment.csv', index=False)



