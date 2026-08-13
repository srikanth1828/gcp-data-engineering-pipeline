from google.cloud import bigquery


def load_to_bigquery(
    dataframe,
    project_id,
    dataset_id,
    table_id
):
    """
    Loads a Pandas DataFrame into Google BigQuery.
    """

    client = bigquery.Client(
        project=project_id
    )

    table_reference = (
        f"{project_id}."
        f"{dataset_id}."
        f"{table_id}"
    )

    job = client.load_table_from_dataframe(
        dataframe,
        table_reference
    )

    job.result()

    print(
        f"Successfully loaded data into "
        f"{table_reference}"
    )


if __name__ == "__main__":
    print(
        "Configure your GCP credentials and "
        "BigQuery project details before running."
    )
