import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load secret keys from .env file
load_dotenv()

print("Connecting to Azure Blob Storage...")

# Connect to Azure
connection_string = os.getenv("AZURE_CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Upload the transformed data
container_name = "education-data"
file_path = "data/raw/education_costs_transformed.csv"
blob_name = "education_costs_transformed.csv"

print("Uploading data to Azure...")

blob_client = blob_service_client.get_blob_client(
    container=container_name, 
    blob=blob_name
)

with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("Data uploaded to Azure Blob Storage successfully!")