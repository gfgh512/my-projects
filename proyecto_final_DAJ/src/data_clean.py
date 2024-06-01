"""
Scrip to clean data
1) Create only date col
2) order cols
3) clean data: Integrate the two previous functions
4) save_clean_data: Save the data to a parquet file
"""
import pandas as pd
from tqdm import tqdm
from generals import DATA_RANGE


RAW_DATA_PATH = "./proyecto_final_DAJ/files_dump/raw_data/"
CLEAN_DATA_PATH = "./proyecto_final_DAJ/files_dump/clean_data/"
VEH_TYPE = "yellow_tripdata_"


def create_date_col(df_: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column with only the date part of the 'tpep_pickup_datetime' column.

    Args:
        df_ (pd.DataFrame): The DataFrame to modify.

    Returns:
        pd.DataFrame: The modified DataFrame.
    """
    df_["tpep_pickup_date"] = df_["tpep_pickup_datetime"].dt.date
    return df_


def order_cols(df_: pd.DataFrame) -> pd.DataFrame:
    """
    Move the last column to the 4th position.

    Args:
        df_ (pd.DataFrame): The DataFrame to modify.

    Returns:
        pd.DataFrame: The modified DataFrame.
    """
    # cols in lower case
    cols = df_.columns.tolist()
    cols = cols[:2] + cols[-1:] + cols[2:-1]
    df_ = df_[cols]
    df_.columns = df_.columns.str.lower()
    return df_

#TODO: Manage null values
#DETAIL:  La fila que falla contiene (2995024, 1, 2023-01-01 00:02:40, 2023-01-01, 2023-01-01 00:30:36, null, 0.00, 142, 79, null, null, 0, 20.13, 0.00, 0.50, 1.00, 0.00, 0.00, 24.13, null, null).

def clean_data(df_: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the data by creating a new column with only the date part of the 'tpep_pickup_datetime' column
    and moving the last column to the 4th position.

    Args:
        df_ (pd.DataFrame): The DataFrame to modify.

    Returns:
        pd.DataFrame: The modified DataFrame.
    """
    df_ = create_date_col(df_)
    df_ = order_cols(df_)
    return df_


def save_clean_data(data_range_: list = DATA_RANGE) -> None:
    """
    Save a DataFrame to a parquet file.

    Args:
        df_ (pd.DataFrame): The DataFrame to save.
        file_name (str): The name of the file to save the DataFrame to.
    """
    for date in tqdm(data_range_):
        file_name = f"{VEH_TYPE}{date}.parquet"
        df = pd.read_parquet(
            f"{RAW_DATA_PATH}{file_name}"
        )
        df = clean_data(df)
        df.to_parquet(f"{CLEAN_DATA_PATH}{file_name}", index=False)
        #print(f"Data for {date} cleaned and saved successfully")


if __name__ == "__main__":
    save_clean_data()
