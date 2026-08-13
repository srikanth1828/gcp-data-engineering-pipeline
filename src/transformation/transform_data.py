from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def transform_data(input_path):

    spark = SparkSession.builder \
        .appName("Transaction Data Transformation") \
        .getOrCreate()

    # Read CSV file
    df = spark.read.csv(
        input_path,
        header=True,
        inferSchema=True
    )

    # Remove duplicates
    df = df.dropDuplicates()

    # Remove missing values
    df = df.dropna(
        subset=[
            "transaction_id",
            "customer_id",
            "quantity",
            "price"
        ]
    )

    # Convert data types
    df = df.withColumn(
        "quantity",
        col("quantity").cast("integer")
    )

    df = df.withColumn(
        "price",
        col("price").cast("double")
    )

    # Create total amount
    df = df.withColumn(
        "total_amount",
        col("quantity") * col("price")
    )

    return df


if __name__ == "__main__":

    input_path = "data/raw/transactions.csv"

    transformed_df = transform_data(input_path)

    transformed_df.show()

    transformed_df.stop()
