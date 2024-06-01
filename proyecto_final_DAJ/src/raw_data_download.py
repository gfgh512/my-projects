"""
Script for downloading data from the cloudfront server.

This script contains the fallowing functions:

- get_data_month(date_: str) -> None:
    This function takes a date in 'YYYYMM' format as input and downloads the
    corresponding data for that month from the cloudfront server. The downloaded
    data is saved in a .parquet file in the local directory.

- get_data_range(start_date_: str, end_date_: str) -> None:
    This function takes a start date and an end date in 'YYYYMM' format as input
    and downloads the data for each month in the range from the cloudfront server.
    The downloaded data is saved in .parquet files in the local directory.

Dependencies:
- os: For interacting with the operating system.
- logging: For logging informational, warning, and error messages.
- datetime: For working with date and time objects.
- dateutil.relativedelta: For performing date and time operations.
- requests: For making HTTP requests.
"""
import os
import logging
import requests
from generals import DATA_RANGE


BASE_LINK = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
VEH_TYPE = "yellow_tripdata_"
RAW_DATA_PATH = "./proyecto_final_DAJ/files_dump/raw_data/"

# Configuración del logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Crea un manejador de consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
# Agrega el manejador al logger
logger.addHandler(console_handler)


def get_data_month(date_: str) -> None:
    """
    Downloads the data for a specific month.

    Args:
        date_ (str): The date in the format 'YYYY-MM'.

    Returns:
        None
    """
    url = f"{BASE_LINK}{VEH_TYPE}{date_}.parquet"
    file_name = f"{VEH_TYPE}{date_}.parquet"
    path = os.path.join(RAW_DATA_PATH, file_name)

    # Download the file
    with requests.get(url, stream=True, timeout=30) as r:
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024**2):
                    f.write(chunk)
        else:
            if os.path.exists(path):
                os.remove(path)
            print(f"Error al descargar el archivo: {r.status_code}")
            r.raise_for_status()
    logger.info("Archivo %s descargado correctamente", file_name)


def get_data_range(data_range: list = DATA_RANGE) -> None:
    """
    Retrieves data for a given range of dates.

    Args:
        start_date_ (str): The start date of the range in the format 'YYYY-MM-DD'.
        end_date_ (str): The end date of the range in the format 'YYYY-MM-DD'.

    Returns:
        None
    """
    for date in data_range:
        if os.path.exists(os.path.join(RAW_DATA_PATH, f"{VEH_TYPE}{date}.parquet")):
            logger.info("El archivo %s ya existe", f"{VEH_TYPE}{date}.parquet")
        else:
            get_data_month(date)


if __name__ == "__main__":
    get_data_range()
