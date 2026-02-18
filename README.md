# 🌦️ End-to-End Modern Weather Data Pipeline

A full-stack data engineering project that automates weather data ingestion, transformation, and visualization using the **Modern Data Stack (MDS)**.

## 🏗️ Architecture
- **Orchestration:** [Apache Airflow](https://airflow.apache.org/) (Ingests raw data via API)
- **Data Warehouse:** [PostgreSQL](https://www.postgresql.org/) (Bronze/Silver/Gold layers)
- **Transformation:** [dbt (data build tool)](https://www.getdbt.com/) (Models hourly weather trends)
- **Visualization:** [Metabase](https://www.metabase.com/) (Live dashboards and analytics)
- **Infrastructure:** [Docker Compose](https://www.docker.com/)

## 🚀 Features
- **Automated Ingestion:** Python scripts in Airflow fetch real-time weather data.
- **SQL Transformations:** dbt cleans raw JSON/CSV data into structured Silver tables and aggregates them into Gold-level summary tables.
- **Hourly Analytics:** The pipeline groups data by orecast_time to visualize temperature fluctuations throughout the day.
- **Containerized Stack:** The entire environment is portable and reproducible via Docker.

## 🛠️ Setup & Usage
1. Clone the repository.
2. Run docker-compose up -d.
3. Access Airflow at localhost:8080 to trigger the ingestion DAG.
4. Run dbt models: docker exec -it <container_name> dbt run.
5. View dashboards at localhost:3000.