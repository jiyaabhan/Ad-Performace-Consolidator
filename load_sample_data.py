import pandas as pd

# Load your two datasets
meta_df = pd.read_csv('meta_sample_data.csv')
ab_df = pd.read_csv('multi_platform_sample_data.csv')

# === Part 1: Process meta_sample_data.csv (detailed Meta ads) ===
meta_processed = meta_df[['campaign_id', 'impressions', 'clicks', 'spent', 'approved_conversion']].copy()
meta_processed = meta_processed.rename(columns={
    'campaign_id': 'campaign_name',
    'spent': 'spend',
    'approved_conversion': 'conversions'
})
meta_processed['platform'] = 'Meta'
meta_processed['campaign_name'] = 'Meta_Campaign_' + meta_processed['campaign_name'].astype(str)
meta_processed['revenue'] = meta_processed['conversions'] * 22.0  # Realistic AOV for e-commerce

# === Part 2: Process multi_platform_sample_data.csv ===
# Facebook part
fb_ab = ab_df[[
    'facebook_ad_campaign', 'facebook_ad_views', 'facebook_ad_clicks',
    'facebook_ad_conversions', 'facebook_cost_per_ad'
]].copy()
fb_ab = fb_ab.rename(columns={
    'facebook_ad_campaign': 'campaign_name',
    'facebook_ad_views': 'impressions',
    'facebook_ad_clicks': 'clicks',
    'facebook_ad_conversions': 'conversions',
    'facebook_cost_per_ad': 'spend'
})
fb_ab['platform'] = 'Meta'
fb_ab['revenue'] = fb_ab['conversions'] * 18.0

# Google part
google_ab = ab_df[[
    'adword_ad_campaign', 'adword_ad_views', 'adword_ad_clicks',
    'adword_ad_conversions', 'adword_cost_per_ad'
]].copy()
google_ab = google_ab.rename(columns={
    'adword_ad_campaign': 'campaign_name',
    'adword_ad_views': 'impressions',
    'adword_ad_clicks': 'clicks',
    'adword_ad_conversions': 'conversions',
    'adword_cost_per_ad': 'spend'
})
google_ab['platform'] = 'Google'
google_ab['revenue'] = google_ab['conversions'] * 15.0

# Combine all three sources
combined_df = pd.concat([meta_processed, fb_ab, google_ab], ignore_index=True)

# Final columns
combined_df = combined_df[[
    'platform', 'campaign_name', 'spend', 'impressions',
    'clicks', 'conversions', 'revenue'
]]

# Save raw combined data
combined_df.to_csv('raw_ad_data.csv', index=False)

print("Successfully combined both datasets!")
print(f"Total rows: {len(combined_df)}")
print(f"Meta rows: {len(combined_df[combined_df['platform'] == 'Meta'])}")
print(f"Google rows: {len(combined_df[combined_df['platform'] == 'Google'])}")
print("\nFirst 10 rows:")
print(combined_df.head(10))