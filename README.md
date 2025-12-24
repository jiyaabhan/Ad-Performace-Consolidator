## Social Media Ad Performance Consolidator

A simple Python tool that automates a common marketing task: combining ad data from Meta (Facebook) and Google Ads, then calculating key metrics like ROI and CPA, and identifying top-performing campaigns from the sample data I have loaded

## Why This Project?
Marketers often manually download reports from multiple platforms, copy-paste into Excel, and calculate metrics. This script automates that entire process

## What It Does
- Loads and combines public sample ad data from Meta and Google
- Calculates ROI, actual CPA, and flags campaigns vs. a target CPA
- Stores data in a SQLite database
- Shows a console dashboard with top campaigns and platform summaries


## How to Run
1. Clone the repo
2. Create virtual env: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install: `pip install pandas sqlalchemy`
5. Run in order:
   ```bash
   python load_sample_data.py
   python clean_and_calculate.py
   python load_to_sql.py
   python dashboard.py

## Data Sources
Meta data: https://www.kaggle.com/datasets/madislemsalu/facebook-ad-campaign
Multi-platform (Google + Meta): https://www.kaggle.com/datasets/shubhamdamai/ab-testing-analysis-facebook-vs-adword
