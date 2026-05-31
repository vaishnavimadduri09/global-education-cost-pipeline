import psycopg2
import pandas as pd

print("Connecting to PostgreSQL...")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres123"
)

cursor = conn.cursor()

print("Creating table...")

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS education_costs (
        country VARCHAR(100),
        university VARCHAR(200),
        tuition_usd FLOAT,
        living_cost_usd FLOAT,
        currency VARCHAR(10),
        tuition_usd_converted FLOAT,
        living_cost_usd_converted FLOAT,
        total_cost_usd FLOAT
    )
""")

print("Loading data into PostgreSQL...")

# Load transformed data
df = pd.read_csv("data/raw/education_costs_transformed.csv")

# Insert each row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO education_costs VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("Data loaded into PostgreSQL successfully!")