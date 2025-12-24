import pandas as pd

df = pd.read_csv('raw_ad_data.csv')

# Clean
df.fillna(0, inplace=True)
df = df.astype({
    'spend': float, 'impressions': int, 'clicks': int,
    'conversions': int, 'revenue': float
})

# E-commerce calculations
target_cpa = float(input("Enter target Cost Per Acquisition: "))
df['roi'] = (df['revenue'] - df['spend']) / df['spend'].replace(0, 1)
df['actual_cpa'] = df['spend'] / df['conversions'].replace(0, 1)
df['cpa_status'] = df.apply(
    lambda row: 'Over Target' if row['actual_cpa'] > target_cpa else 'Under Target',
    axis=1
)

df.to_csv('cleaned_ad_data.csv', index=False)
print("Cleaned + metrics added → cleaned_ad_data.csv")
print(df[['campaign_name', 'platform', 'roi', 'actual_cpa', 'cpa_status']].head(10))