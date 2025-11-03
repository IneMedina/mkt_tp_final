import pandas as pd
import os


os.makedirs('DW', exist_ok=True)


product = pd.read_csv('raw/product.csv')
category = pd.read_csv('raw/product_category.csv')


category = category.rename(columns={'name': 'category_name'})


category = category.merge(
    category[['category_id', 'category_name']].rename(
        columns={'category_id': 'parent_id', 'category_name': 'parent_category_name'}
    ),
    on='parent_id',
    how='left'
)

dim_producto = product.merge(category[['category_id', 'category_name', 'parent_category_name']],
                             on='category_id',
                             how='left')


dim_producto = dim_producto[[
    'product_id',
    'sku',
    'name',
    'category_name',
    'parent_category_name',
    'list_price',
    'status',
    'created_at'
]]


dim_producto.to_csv('DW/DimProducto.csv', index=False)


