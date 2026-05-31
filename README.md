# 🎓 Global Education Cost Intelligence Pipeline

## Problem
Students applying abroad struggle to compare education costs across countries due to different currencies and data sources.

## Solution
A complete data pipeline that collects, validates, transforms and visualizes university cost data from 10 countries!

## Pipeline Architecture
CSV Data
↓
Python Extraction
↓
Data Validation
↓
Transformation (Currency Conversion)
↓
Azure Blob Storage
↓
PostgreSQL
↓
Power BI Dashboard
## Countries Covered
🇺🇸 USA | 🇬🇧 UK | 🇩🇪 Germany | 🇦🇺 Australia | 🇨🇦 Canada
🇮🇳 India | 🇫🇷 France | 🇯🇵 Japan | 🇨🇳 China | 🇧🇷 Brazil

## Project Files
- **extract.py** — Extracts education cost data
- **validate.py** — Validates data quality
- **transform.py** — Converts all costs to USD
- **load_blob.py** — Uploads data to Azure Blob Storage
- **load_postgres.py** — Loads data into PostgreSQL

## Tools Used
- Python
- Azure Blob Storage
- PostgreSQL
- Power BI
- Git & GitHub

## Key Findings
- Harvard University (USA) is the most expensive at $72,000/year
- IIT Delhi (India) is the most affordable at $60/year
- European universities offer great value compared to USA/UK

## Author
Vaishnavi Madduri