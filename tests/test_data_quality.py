from pyspark.sql import SparkSession
from src.data_quality.data_quality_checks import run_data_quality_checks


def test_valid_data_quality():

    spark = (
        SparkSession.builder
        .appName("DataQualityTest")
        .master("local[*]")
        .getOrCreate()
    )

    data = [
        (1001, "C001", 2, 100.0),
        (1002, "C002", 1, 200.0),
    ]

    columns = [
        "transaction_id",
        "customer_id",
        "quantity",
        "price",
    ]

    df = spark.createDataFrame(data, columns)

    result = run_data_quality_checks(df)

    assert result is True

    spark.stop()
