"Script to load the data into the database"
from generals import DATA_RANGE, CONN
import pandas as pd
from tqdm import tqdm

CLEAN_DATA_PATH = "./proyecto_final_DAJ/files_dump/clean_data/"
VEH_TYPE = "yellow_tripdata_"
TABLE_NAME = "yellow_taxi_trips"

def upload_month(date_: str) -> None:
    """
    Upload the data for a specific month to the database.

    Args:
        date_ (str): The date in the format 'YYYY-MM'.

    Returns:
        None
    """
    file_name = f"{VEH_TYPE}{date_}.parquet"
    df = pd.read_parquet(f"{CLEAN_DATA_PATH}{file_name}")
    df.to_sql(
        name=TABLE_NAME,
        con=CONN,
        schema="yellow",
        if_exists="append",
        index=False
    )
    print(f"Data for {date_} uploaded successfully")

def upload_month_chunks(date_: str, chunk_size_ = 10000) -> None:
    """
    Upload the data for a specific month to the database in chunks.

    Args:
        date_ (str): The date in the format 'YYYY-MM'.
        chunk_size_ (int): The size of the chunks to upload.

    Returns:
        None
    """
    file_name = f"{VEH_TYPE}{date_}.parquet"
    df = pd.read_parquet(f"{CLEAN_DATA_PATH}{file_name}")
    total_rows = df.shape[0]
    for i in tqdm(range(0, total_rows, chunk_size_)):
        df_chunk = df[i:i+chunk_size_] # chunk length
        df_chunk.to_sql(
            name=TABLE_NAME,
            con=CONN,
            schema="yellow",
            if_exists="append",
            index=False
        )



if __name__ == "__main__":
    for date in tqdm(DATA_RANGE):
        upload_month_chunks(date)
