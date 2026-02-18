# End-to-End Modern Weather Data Pipeline

A full-stack data engineering project that automates weather data ingestion, transformation, and visualization using the Modern Data Stack (MDS).

### 🛠️ Project Status
[![Project Checkup](https://github.com/hizkyas/weather-data-pipeline-end-to-end/actions/workflows/checkup.yml/badge.svg)](https://github.com/hizkyas/weather-data-pipeline-end-to-end/actions)

---

### Architecture
* **Orchestration:** [Apache Airflow](https://airflow.apache.org/) (Ingests raw data via API)
* **Data Warehouse:** [PostgreSQL](https://www.postgresql.org/) (Bronze/Silver/Gold layers)
* **Transformation:** [dbt (data build tool)](https://www.getdbt.com/) (Models hourly weather trends)
* **Visualization:** [Metabase](https://www.metabase.com/) (Live dashboards and analytics)
* **Infrastructure:** [Docker Compose](https://docs.docker.com/compose/)
