import pandas as pd
import os


nps = pd.read_csv('RAW/nps_response.csv')


nps['date_id'] = pd.to_datetime(nps['responded_at']).dt.strftime('%Y%m%d').astype(int)





fact_nps = nps[['nps_id', 'customer_id', 'channel_id', 'date_id', 'score']]

fact_nps.to_csv('DW/Fact_NPS.csv', index=False)

