# Project Architecture

## Overview

This project demonstrates an end-to-end data engineering workflow for processing transaction data.

The pipeline is designed with separate components for ingestion, transformation, data quality validation, orchestration, and analytics.

## Architecture Flow

```text
                    ┌──────────────────────┐
                    │   Raw Transaction    │
                    │        Data          │
                    │  transactions.csv    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Ingestion       │
                    │    Python / Pandas   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Transformation     │
                    │       PySpark        │
                    │                      │
                    │ • Remove duplicates  │
                    │ • Handle null values │
                    │ • Cast data types    │
                    │ • Calculate revenue  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Data Quality      │
                    │                      │
                    │ • Missing values     │
                    │ • Duplicate IDs      │
                    │ • Invalid quantity   │
                    │ • Invalid price      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Airflow        │
                    │    Orchestration     │
                    │                      │
                    │ Schedule & Monitor   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      BigQuery        │
                    │   Data Warehouse     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Analytics Layer    │
                    │  Sales Summary SQL   │
                    └──────────────────────┘
```

## Components

### Data Ingestion

The ingestion component reads raw transaction data from a CSV source.

**Location:**

`src/ingestion/ingest_data.py`

### Data Transformation

PySpark is used to clean and transform the raw transaction data.

Key transformations include:

* Removing duplicate records
* Handling missing values
* Converting numeric data types
* Creating the `total_amount` field

**Location:**

`src/transformation/transform_data.py`

### Data Quality

The data quality module validates the transformed dataset before it moves to the next stage.

Checks include:

* Missing transaction IDs
* Duplicate transaction IDs
* Invalid quantity values
* Invalid price values

**Location:**

`src/data_quality/data_quality_checks.py`

### Orchestration

Apache Airflow is used to define the pipeline workflow.

**Location:**

`airflow/dags/transaction_pipeline_dag.py`

### Data Warehouse

The BigQuery loading component is designed to load processed data into a BigQuery table.

**Location:**

`src/loading/load_to_bigquery.py`

### Analytics

The SQL layer creates an analytics-ready daily sales summary.

Metrics include:

* Total transactions
* Total customers
* Total items sold
* Total revenue
* Average transaction value

**Location:**

`sql/sales_summary.sql`

## Current Implementation

The local PySpark pipeline has been tested successfully with the sample transaction dataset.

The Airflow and BigQuery components are included as project architecture components and require additional environment and cloud configuration before they can be executed.

## Future Enhancements

* Connect Google Cloud Storage for raw data ingestion
* Configure BigQuery credentials and dataset
* Execute the Airflow DAG in a local or cloud environment
* Add dbt transformation models
* Add automated testing
* Add CI/CD using GitHub Actions or Cloud Build
* Add monitoring and alerting
