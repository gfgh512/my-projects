from sqlalchemy import text
import pandas as pd
from generals import CONN


QUERY = """
select vendorid, count(1) from tlc_ny.yellow.taxi_trips
group by vendorid
    """

def query_result ():
    with CONN.connect() as connection:
        result = connection.execute(text(QUERY))
        return result.fetchall()


def query_df ():
    return pd.read_sql(QUERY, CONN)

    
if __name__ == "__main__":
    print(query_df())
