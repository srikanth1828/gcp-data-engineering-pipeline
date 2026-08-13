from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="transaction_data_pipeline",
    description="Orchestrates the PySpark transaction data pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["data-engineering", "pyspark"],
) as dag:

    run_transaction_pipeline = BashOperator(
        task_id="run_transaction_pipeline",
        bash_command="python src/main.py",
    )

    run_transaction_pipeline
