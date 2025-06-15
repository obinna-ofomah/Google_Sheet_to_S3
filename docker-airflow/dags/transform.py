import pandas as pd

def format_columns(record):
    """
    A function that formats the columns of data.
    Args:
        Records in Python List
    Return:
        Records in Pandas DataFrame
    """

    # Read all records into DataFrame
    df = pd.DataFrame(record)

    # Extract all the columns and convert into a List
    df_columns = list(df.columns)

    # Format the DataFrame columns
    for i in range(len(df_columns)):
        df_columns[i] = df_columns[i].strip().replace(' ', '_')

    # Re-assign the formatted columns to the Dataframe columns
    df.columns = df_columns
    return df