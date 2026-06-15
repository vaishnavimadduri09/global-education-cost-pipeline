import pandas as pd

def validate(df):
    print("🔍 Validating data...")

    # Check for nulls
    nulls = df.isnull().sum()
    if nulls.any():
        print(f"⚠️ Null values found:")
        print(nulls[nulls > 0])
    else:
        print("✅ No null values found!")

    # Check for duplicates
    dupes = df.duplicated().sum()
    if dupes > 0:
        print(f"⚠️ {dupes} duplicate rows found!")
    else:
        print("✅ No duplicates found!")

    # Check row count
    if len(df) == 0:
        raise ValueError("❌ Dataset is empty!")
    else:
        print(f"✅ Dataset has {len(df)} rows")

    print("✅ Validation complete!")
    return True

if __name__ == "__main__":
    df = pd.read_csv("data/cwurData.csv")
    validate(df)