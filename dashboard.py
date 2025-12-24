import sqlite3

conn = sqlite3.connect('ad_performance.db')
cursor = conn.cursor()

print("=== Top 10 Campaigns by ROI ===")
cursor.execute('''
    SELECT campaign_name, platform, roi, actual_cpa, cpa_status
    FROM cleaned_data
    ORDER BY roi DESC
    LIMIT 10
''')
for row in cursor.fetchall():
    print(row)

print("\n=== Platform Summary ===")
cursor.execute('SELECT * FROM platform_summary')
for row in cursor.fetchall():
    print(row)

conn.close()
