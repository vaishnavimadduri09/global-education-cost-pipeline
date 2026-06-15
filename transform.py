import pandas as pd

def transform(df):
    print("🔄 Transforming data...")

    # Fix missing values in broad_impact
    df["broad_impact"] = df["broad_impact"].fillna(0)

    # Standardize country names
    df["country"] = df["country"].str.strip().str.title()

    # Standardize institution names
    df["institution"] = df["institution"].str.strip()

    # Add a total score rank category
    df["rank_category"] = pd.cut(
        df["world_rank"],
        bins=[0, 100, 500, 1000, 2200],
        labels=["Top 100", "Top 500", "Top 1000", "Rest"]
    )

    # Keep only useful columns
    df = df[["world_rank", "institution", "country", 
             "score", "year", "broad_impact", "rank_category"]]

    print(f"✅ Transformed data — {len(df)} rows ready")
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/cwurData.csv")
    from validate import validate
    validate(df)
    df = transform(df)
    print(df.head())