import pandas as pd

print("Starting transformation...")

# Load the data
df = pd.read_csv("data/raw/education_costs.csv")

# Exchange rates to USD
exchange_rates = {
    "USD": 1.0,
    "GBP": 1.27,
    "EUR": 1.08,
    "AUD": 0.65,
    "CAD": 0.74,
    "INR": 0.012,
    "JPY": 0.0067,
    "CNY": 0.14,
    "BRL": 0.20
}

print("Converting all costs to USD...")

# Convert tuition to USD
df["tuition_usd_converted"] = df.apply(
    lambda row: row["tuition_usd"] * exchange_rates[row["currency"]], axis=1
)

# Convert living costs to USD
df["living_cost_usd_converted"] = df.apply(
    lambda row: row["living_cost_usd"] * exchange_rates[row["currency"]], axis=1
)

# Calculate total cost
df["total_cost_usd"] = df["tuition_usd_converted"] + df["living_cost_usd_converted"]

# Save transformed data
df.to_csv("data/raw/education_costs_transformed.csv", index=False)

print("Transformation complete!")
print(df[["country", "university", "total_cost_usd"]])