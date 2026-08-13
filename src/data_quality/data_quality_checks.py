from pyspark.sql.functions import col


def run_data_quality_checks(df):
    """
    Run basic data quality checks on the
    transformed transaction dataset.
    """

    print("\nRunning Data Quality Checks...")

    # Check for missing transaction IDs
    missing_transaction_ids = df.filter(
        col("transaction_id").isNull()
    ).count()

    print(
        f"Missing transaction IDs: "
        f"{missing_transaction_ids}"
    )

    # Check for duplicate transaction IDs
    duplicate_transaction_ids = (
        df.groupBy("transaction_id")
        .count()
        .filter(col("count") > 1)
        .count()
    )

    print(
        f"Duplicate transaction IDs: "
        f"{duplicate_transaction_ids}"
    )

    # Check for invalid quantities
    invalid_quantity = df.filter(
        col("quantity") <= 0
    ).count()

    print(
        f"Invalid quantity records: "
        f"{invalid_quantity}"
    )

    # Check for invalid prices
    invalid_price = df.filter(
        col("price") <= 0
    ).count()

    print(
        f"Invalid price records: "
        f"{invalid_price}"
    )

    # Final validation
    if (
        missing_transaction_ids == 0
        and duplicate_transaction_ids == 0
        and invalid_quantity == 0
        and invalid_price == 0
    ):
        print("Data Quality Checks Passed!")
        return True

    print("Data Quality Checks Failed!")
    return False
