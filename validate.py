import pandas as pd

print("Starting data validation...")

# Load the data
df = pd.read_csv("data/raw/education_costs.csv")

# Check 1: Look for missing values
print("Checking for missing values...")
missing = df.isnull().sum()
print(missing)

# Check 2: Check how many rows and columns we have
print(f"Total rows: {df.shape[0]}")
print(f"Total columns: {df.shape[1]}")

print("Validation complete!")