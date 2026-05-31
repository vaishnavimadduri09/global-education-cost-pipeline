import pandas as pd
import requests

print("Starting data extraction...")

# Download education cost data
url = "https://raw.githubusercontent.com/dsrscientist/dataset1/master/education.csv"

response = requests.get(url)

print("Data extracted successfully!")