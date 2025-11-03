import pandas as pd
import os


nps = pd.read_csv('RAW/nps_response.csv')


nps['date_id'] = pd.to_datetime(nps['responded_at']).dt.strftime('%Y%m%d').astype(int)


nps['is_promoter'] = (nps['score'] >= 9).astype(int)
nps['is_detractor'] = (nps['score'] <= 6).astype(int)


fact_nps = nps[['nps_id', 'customer_id', 'channel_id', 'date_id', 'score', 'is_promoter', 'is_detractor']]

fact_nps.to_csv('DW/Fact_NPS.csv', index=False)

