# Modern Weather Data Pipeline 🌦️

An end-to-end data engineering project that automates weather data ingestion and transformation. This pipeline demonstrates a modern ELT (Extract, Load, Transform) pattern using industry-standard orchestration and containerization.

## 🏗️ The Stack
* **Orchestration:** [Apache Airflow](https://airflow.apache.org/) (Running the `LocalExecutor`)
* **Ingestion:** Python-based extraction from the **Open-Meteo API**
* **Storage:** **PostgreSQL 15** (Data Warehouse)
* **Transformation:** **dbt (data build tool)** for SQL modeling
* **Environment:** **Docker Desktop** & **PowerShell**

## 🚀 Key Features
* **Automated Library Injection:** Uses `_PIP_ADDITIONAL_REQUIREMENTS` to dynamically install `pandas`, `requests`, and `dbt-postgres` on container startup.
* **Layered Architecture:**
    * **Bronze Layer:** Raw JSON data ingested into Postgres.
    * **Silver Layer:** dbt-transformed tables for clean, analytics-ready weather metrics.
* **Resilient Design:** Postgres health checks ensure the database is fully initialized before Airflow services start.

## 🛠️ Installation & Setup

### 1. Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* PowerShell (Standard on Windows)

### 2. Launch the Pipeline
Clone the repository and spin up the environment:
```powershell
git clone [https://github.com/YOUR_USERNAME/modern-weather-data-pipeline.git](https://github.com/YOUR_USERNAME/modern-weather-data-pipeline.git)
cd modern-weather-data-pipeline
docker-compose up -d


Gemini said
I can't provide a direct file download link (like a .zip or .exe), but I can generate the file content for you in a way that allows you to save it instantly using PowerShell.

Since you are using PowerShell, you don't even need to open an editor. Just copy and paste the entire block below into your terminal and press Enter. It will create the file for you:

PowerShell
$readmeContent = @"
# Modern Weather Data Pipeline 🌦️

An end-to-end data engineering project that automates weather data ingestion and transformation. This pipeline demonstrates a modern ELT (Extract, Load, Transform) pattern using industry-standard orchestration and containerization.

## 🏗️ The Stack
* **Orchestration:** [Apache Airflow](https://airflow.apache.org/) (Running the LocalExecutor)
* **Ingestion:** Python-based extraction from the **Open-Meteo API**
* **Storage:** **PostgreSQL 15** (Data Warehouse)
* **Transformation:** **dbt (data build tool)** for SQL modeling
* **Environment:** **Docker Desktop**, **PowerShell**, and **Antigravity IDE**

## 🚀 Key Features
* **Automated Library Injection:** Dynamically installs pandas, requests, sqlalchemy, and dbt-postgres on container startup.
* **Layered Architecture:**
    * **Bronze Layer:** Raw JSON data ingested from API into Postgres.
    * **Silver Layer:** Cleaned, analytics-ready weather metrics transformed via dbt.
* **Resilient Design:** Integrated Docker health checks ensure the database is fully initialized before Airflow services start.

## 🛠️ Installation & Setup

### 1. Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* PowerShell (Standard on Windows)

### 2. Launch the Pipeline
Spin up the environment from your terminal:
```powershell
docker-compose up -d
3. Initialize Airflow User
Once the containers are healthy (check docker ps), create your admin account:

PowerShell
docker exec -it modern_data_pipeline-airflow-webserver-1 airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@example.com --password admin
4. Run Transformations
After the Airflow DAG runs successfully (Green Circle), execute the dbt models:

PowerShell
docker exec -it modern_data_pipeline-airflow-webserver-1 dbt run --project-dir /opt/airflow/dbt --profiles-dir /opt/airflow/dbt
📊 Pipeline Monitoring
Airflow UI: http://localhost:8080

Database: Access via port 5432 (User: airflow, Pass: airflow)

🛡️ Troubleshooting
The project is configured to bypass common Windows-to-Linux pathing issues by defining _PIP_ADDITIONAL_REQUIREMENTS directly in the docker-compose.yaml environment.
"@

$readmeContent | Out-File -FilePath README.md -Encoding utf8
Write-Host "README.md has been created successfully!" -ForegroundColor Green


---

### What to do next:
After running that command, your file is ready. You can finish the GitHub process by running:

```powershell
git add README.md
git commit -m "docs: auto-generated README via PowerShell"
git push origin main