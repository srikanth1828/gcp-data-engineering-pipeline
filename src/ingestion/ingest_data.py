"""
Data ingestion module.

This script reads raw customer transaction data
and prepares it for downstream processing.
"""

import pandas as pd


def load_data(file_path):
    """Load raw CSV data."""
    df = pd.read_csv(file_path)

    print(f"Loaded {len(df)} records")
    return df


if __name__ == "__main__":
    file_path = "data/raw/transactions.csv"
    load_data(file_path)
