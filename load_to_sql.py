import pandas as pd
from sqlalchemy import create_engine
import sqlite3

raw_df = pd.read_csv('raw_ad_data.csv')
cleaned_df = pd.read_csv('cleaned_ad_data.csv')

engine = create_engine('sqlite:///ad_performance.db')
raw_df.to_sql('raw_data', engine, if_exists='replace', index=False)
cleaned_df.to_sql('cleaned_data', engine, if_exists='replace', index=False)

conn = sqlite3.connect('ad_performance.db')
conn.execute('''
    CREATE VIEW IF NOT EXISTS platform_summary AS
    SELECT platform,
           COUNT(*) as total_campaigns,
           SUM(spend) as total_spend,
           SUM(conversions) as total_conversions,
           SUM(revenue) as total_revenue,
           AVG(roi) as avg_roi
    FROM cleaned_data
    GROUP BY platform
''')
conn.close()
print("Data loaded into ad_performance.db")