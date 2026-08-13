from transformation.transform_data import transform_data
from data_quality.data_quality_checks import run_data_quality_checks


def main():
    print("Starting Data Engineering Pipeline...")

    # Step 1: Transform data
    input_path = "data/raw/transactions.csv"
    transformed_df = transform_data(input_path)

    # Step 2: Run data quality checks
    quality_passed = run_data_quality_checks(transformed_df)

    if quality_passed:
        print("\nPipeline completed successfully!")

        print("\nTransformed Data:")
        transformed_df.show()

    else:
        print("\nPipeline failed due to data quality issues.")

    # Stop Spark session
    transformed_df.sparkSession.stop()


if __name__ == "__main__":
    main()
