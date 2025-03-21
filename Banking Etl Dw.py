import os
import pandas as pd
import boto3
import psycopg2
from sqlalchemy import create_engine
from datetime import datetime
import config  # AWS & DB credentials (dummy values in GitHub)

def extract_data():
    """Extracts sales transactions from AWS S3."""
    try:
        s3 = boto3.client('s3', aws_access_key_id=config.AWS_ACCESS_KEY,
                          aws_secret_access_key=config.AWS_SECRET_KEY)
        obj = s3.get_object(Bucket=config.S3_BUCKET, Key='sales_data.csv')
        df = pd.read_csv(obj['Body'])
        print("Data extracted successfully from S3.")
        return df
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

def transform_data(df):
    """Cleans and transforms sales data."""
    if df is None:
        print("No data to transform.")
        return None
    try:
        df.dropna(inplace=True)
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
        df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
        df['Sales'] = df['Sales'].astype(float)
        df['Profit'] = df['Profit'].astype(float)
        df['Discount'] = df['Discount'].astype(float)
        df['Quantity'] = df['Quantity'].astype(int)
        df['Profit Margin'] = df['Profit'] / df['Sales']
        df['Processing Time (Days)'] = (df['Ship Date'] - df['Order Date']).dt.days
        print("Data transformation completed.")
        return df
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None

def load_data(df):
    """Loads transformed data into AWS Redshift."""
    if df is None:
        print("No data to load.")
        return
    try:
        engine = create_engine(f'postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}')
        df.to_sql('sales_transactions', engine, index=False, if_exists='replace')
        print("Data loaded into Redshift successfully.")
    except Exception as e:
        print(f"Error loading data: {e}")

def main():
    """Main ETL pipeline function."""
    print("Starting ETL pipeline...")
    df = extract_data()
    df = transform_data(df)
    load_data(df)
    print("ETL pipeline completed.")

if __name__ == "__main__":
    main()
