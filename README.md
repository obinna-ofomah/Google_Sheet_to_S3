# Project Title
- Googlesheet to S3 Pipeline

---
## Project Description
- An ETL Pipeline that fetches data from a Google Sheet, transforms it and loads same to AWS S3 Bucket

---
## Project Requirements (Libraries and Tools)
- Python 3.0+
- Gpsread
- Awswrangler
- Google Sheet API
- Google Drive API
- Pandas
- Google Sheet
- AWS S3 Bucket
- Docker
- Terraform
- Apache Airflow

---
## Project Activities 
- 🔨 Install the required python libraries and Google APIs
- 🌏 Connect Google sheet to Python using the APIs
- 📖Export sheet to pandas DataFrame
- 📓Format the Headers or Columns by - remove the leading and trailing spaces in each column, and replace the inner space with an underscore ('_')
- 🔧Provision an S3 Bucket using Terraform
- 💂Authenticate the IAM User using the Boto3 Library
- 🪣Covert file to Parquet and Write same to S3 Bucket using the Awswrangler library
- 🧰Package the Application

---