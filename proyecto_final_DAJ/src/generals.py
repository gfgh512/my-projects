"""
Generals functions for the project.

This script contains the fallowing functions:
- generate_dates(start_date_: str, end_date_: str) -> list:
    This function takes a start date and an end date in 'YYYYMM' format as input
    and generates a list of dates between the start date and end date (inclusive).
"""
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

load_dotenv('.env')


def generate_dates(start_date_: str, end_date_: str) -> list:
    """
    Generate a list of dates between the start_date and end_date (inclusive).

    Args:
        start_date_ (str): The start date in the format 'YYYYMM'.
        end_date_ (str): The end date in the format 'YYYYMM'.

    Returns:
        list: A list of dates in the format 'YYYY-MM' between the start_date and end_date.

    Example:
        >>> generate_dates('202101', '202112')
        ['2021-01', '2021-02', '2021-03', '2021-04',
        '2021-05', '2021-06', '2021-07', '2021-08', '2021-09',
        '2021-10', '2021-11', '2021-12']
    """
    start_date_date = datetime.strptime(start_date_, '%Y%m')
    end_date_date = datetime.strptime(end_date_, '%Y%m')
    date_list = []
    while start_date_date <= end_date_date:
        date_list.append(start_date_date.strftime('%Y-%m'))
        #start_date_date = start_date_date + relativedelta(months=1)
        start_date_date += relativedelta(months=1)
    return date_list


POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
DB = "tlc_ny"

db_string = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB}"
CONN = create_engine(db_string)

START_DATE = "202301"
END_DATE = "202303"

DATA_RANGE: list = generate_dates(START_DATE, END_DATE)

if __name__ == "__main__":
    test_query = "SELECT * FROM yellow.taxi_trips limit 1"
    print(pd.read_sql(test_query, CONN))
