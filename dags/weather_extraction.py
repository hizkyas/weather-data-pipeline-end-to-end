from sqlalchemy import create_engine
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import requests
import pandas as pd

def extract_and_load():
    # 1. Extraction from API
    url = "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current_weather=true"
    response = requests.get(url).json()
    current_weather = response['current_weather']
    
    # 2. Transform into a simple DataFrame
    df = pd.DataFrame([current_weather])
    df['ingested_at'] = datetime.now()

    # 3. Load into Postgres
    # Note: We are using the direct engine string to avoid any 'postgres_default' connection issues
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres:5432/airflow')
    
    with engine.begin() as conn:
        df.to_sql('bronze_weather', conn, if_exists='append', index=False)
    print("Successfully loaded data to bronze_weather table.")

with DAG(
    dag_id='weather_ingestion_v1',
    start_date=datetime(2026, 1, 1),
    schedule_interval='@hourly',
    catchup=False
) as dag:

    task_extract = PythonOperator(
        task_id='extract_weather_data',
        python_callable=extract_and_load
    ) # <--- Ensure this is closed properly