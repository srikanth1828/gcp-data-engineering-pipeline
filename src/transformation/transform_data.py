from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def transform_data(input_path):
    """
    Reads raw transaction data and applies
    basic cleaning and transformations.
    """

    spark = SparkSession.builder \
        .appName("Transaction Data Transformation") \
        .getOrCreate()

    # Read raw CSV data
    df = spark.read.csv(
        input_path,
        header=True,
        inferSchema=True
    )

    # Remove duplicate records
    df = df.dropDuplicates()

    # Remove records with missing critical values
    df = df.dropna(
        subset=["transaction_id", "customer_id", "quantity", "price"]
    )

    # Ensure numeric columns have correct data types
    df = df.withColumn("quantity", col("quantity").cast("integer"))
    df = df.withColumn("price", col("price").cast("double"))

    # Create total transaction amount
    df = df.withColumn(
        "total_amount",
        col("quantity") * col("price")
    )

    print("Data transformation completed successfully.")

    return df


if __name__ == "__main__":
    input_path = "data/raw/transactions.csv"

    transformed_df = transform_data(input_path)

    transformed_df.show()

    transformed_df.stop()
