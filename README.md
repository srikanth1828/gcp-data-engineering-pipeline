# GCP Data Engineering Pipeline

An end-to-end data engineering project that processes transaction data using Python and PySpark.

The pipeline performs data ingestion, transformation, and data quality validation to prepare raw transaction data for downstream analytics and cloud data warehouse integration.

## 🚀 Project Overview

This project demonstrates a basic data engineering workflow:

Raw CSV Data → PySpark Transformation → Data Quality Checks → Analytics-Ready Data

The pipeline processes transaction records, cleans the data, validates data quality, and creates a calculated `total_amount` field.

## 🏗️ Project Architecture

```text
                ┌─────────────────────┐
                │   Raw CSV Data      │
                │ transactions.csv    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Data Ingestion    │
                │      Python         │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ PySpark Processing  │
                │ • Remove duplicates │
                │ • Handle nulls      │
                │ • Cast data types   │
                │ • Calculate sales   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Data Quality Checks │
                │ • Missing values    │
                │ • Duplicate IDs     │
                │ • Invalid quantity  │
                │ • Invalid price     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Analytics-Ready Data│
                │    total_amount     │
                └─────────────────────┘
```

## 📂 Project Structure

```text
gcp-data-engineering-pipeline/
│
├── data/
│   └── raw/
│       └── transactions.csv
│
├── src/
│   ├── ingestion/
│   │   └── ingest_data.py
│   │
│   ├── transformation/
│   │   └── transform_data.py
│   │
│   ├── data_quality/
│   │   └── data_quality_checks.py
│   │
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Technologies Used

* Python
* PySpark
* Pandas
* Apache Spark
* Git
* GitHub

## 🔄 Pipeline Workflow

### 1. Data Ingestion

The pipeline reads raw transaction data from a CSV file.

### 2. Data Transformation

The PySpark transformation performs:

* Removes duplicate records
* Removes records with missing critical values
* Converts `quantity` to integer
* Converts `price` to double
* Creates a `total_amount` column

```text
total_amount = quantity × price
```

### 3. Data Quality Checks

The pipeline validates:

* Missing transaction IDs
* Duplicate transaction IDs
* Invalid quantity values
* Invalid price values

The pipeline only completes successfully when all data quality checks pass.

## ▶️ How to Run the Project

### Clone the repository

```bash
git clone https://github.com/srikanth1828/gcp-data-engineering-pipeline.git
```

### Navigate to the project

```bash
cd gcp-data-engineering-pipeline
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Run the pipeline

```bash
python src/main.py
```

## 📊 Sample Output

```text
Starting Data Engineering Pipeline...

Running Data Quality Checks...

Missing transaction IDs: 0
Duplicate transaction IDs: 0
Invalid quantity records: 0
Invalid price records: 0

Data Quality Checks Passed!

Pipeline completed successfully!
```

The output dataset includes the calculated `total_amount` column.

## 🔮 Future Improvements

This project can be extended by adding:

* Google Cloud Storage for raw data ingestion
* BigQuery for data warehousing
* Apache Airflow for orchestration
* dbt for SQL-based transformations
* Automated CI/CD
* Cloud-based monitoring and alerting
* Real-time streaming using Kafka or Pub/Sub

## 👤 Author

**Srikanth Gundoju**

Data Engineer | Python | PySpark | GCP | BigQuery | Apache Airflow
