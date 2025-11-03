import pandas as pd
import os


sessions = pd.read_csv('RAW/web_session.csv')


sessions['date_id'] = pd.to_datetime(sessions['started_at']).dt.strftime('%Y%m%d').astype(int)


fact_actividad = sessions[['session_id', 'customer_id', 'date_id', 'source', 'device']]


fact_actividad.to_csv('DW/Fact_Actividad.csv', index=False)