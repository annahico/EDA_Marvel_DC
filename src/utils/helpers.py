def load_data(filepath):
    """Load a dataset from a CSV file."""
    import pandas as pd
    return pd.read_csv(filepath)


def clean_data(df):
    """Clean dataset by handling missing values and duplicates."""
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df
