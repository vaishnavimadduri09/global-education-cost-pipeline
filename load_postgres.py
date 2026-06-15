from google.cloud import bigquery
import pandas as pd

def load(df):
    print("📤 Loading data into BigQuery...")

    client = bigquery.Client(project="education-pipeline-499514")

    table_id = "education-pipeline-499514.education_costs.university_rankings"

    job = client.load_table_from_dataframe(df, table_id)
    job.result()

    print(f"✅ Loaded {len(df)} rows into BigQuery!")

if __name__ == "__main__":
    from extract import extract
    from validate import validate
    from transform import transform

    df = extract()
    validate(df)
    df = transform(df)
    load(df)