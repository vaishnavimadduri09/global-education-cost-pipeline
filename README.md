# Global Education Cost Intelligence Pipeline

An end-to-end data engineering pipeline that collects, validates, cleans, transforms, and loads real-world university ranking data into a cloud data warehouse using a modern data engineering stack.

## Architecture

Raw CSV Data → Python Extraction → Data Validation → Data Transformation → BigQuery Cloud Warehouse → dbt Models → Analytics Ready Data

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core ETL pipeline development |
| Pandas | Data manipulation and transformation |
| BigQuery | Cloud data warehouse for structured storage |
| Apache Airflow | Pipeline orchestration and scheduling |
| dbt | SQL-based data modeling and transformation |
| Google Cloud | Cloud infrastructure |
| Git/GitHub | Version control and collaboration |

## Dataset

- Source: World University Rankings (CWUR Dataset)
- Size: 2,200 rows spanning multiple years
- Coverage: Top universities from 70+ countries worldwide
- Fields: World rank, institution name, country, score, broad impact, year

## Pipeline Steps

### 1. Extract
Downloads and reads the raw CWUR university ranking dataset from source into a Pandas DataFrame for processing.

### 2. Validate
Performs data quality checks including null value detection, duplicate row identification, row count verification, and column schema validation before any transformations are applied.

### 3. Transform
Cleans and enriches the raw data by standardizing country and institution names, handling missing values in the broad_impact column, and adding a derived rank_category column that classifies universities into Top 100, Top 500, Top 1000, and Rest tiers.

### 4. Load
Loads the cleaned and transformed data into Google BigQuery cloud data warehouse using the BigQuery Python client library, making it queryable at scale.

### 5. dbt Modeling
Applies additional SQL-based transformations using dbt to create analytics-ready tables, adding a score_category column that classifies universities as Excellent, Good, or Average based on their score.

## Project Structure

- extract.py — Handles data extraction from source
- validate.py — Runs data quality and validation checks
- transform.py — Cleans and transforms raw data
- load_postgres.py — Loads transformed data into BigQuery
- models/example/university_rankings.sql — dbt transformation model
- models/example/sources.yml — dbt source definitions
- dbt_project.yml — dbt project configuration
- data/ — Raw and processed data files

## Key Features

- Automated data validation with null and duplicate detection
- Multi-currency normalization and standardization
- Cloud-native storage using Google BigQuery
- Modular pipeline design following ETL best practices
- SQL transformations managed and versioned with dbt
- Pipeline scheduling and orchestration with Apache Airflow

## How to Run

Clone the repository and install the required dependencies. Run each pipeline step in order starting with extraction, followed by validation, transformation, and loading into BigQuery. Finally run the dbt models to apply SQL transformations on top of the loaded data.

## Author

**Vaishnavi Madduri**
Data Engineering | Python | BigQuery | Airflow | dbt | Google Cloud
[LinkedIn](https://linkedin.com/in/vaishnavimadduri) | [GitHub](https://github.com/vaishnavimadduri09)
