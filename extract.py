import pandas as pd
import os

def extract():
    print("📥 Extracting data...")

    df = pd.read_csv("data/cwurData.csv")

    print(f"✅ Extracted {len(df)} rows and {len(df.columns)} columns")
    print(df.head())
    return df

if __name__ == "__main__":
    extract()