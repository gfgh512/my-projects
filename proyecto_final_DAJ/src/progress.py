from sqlalchemy import text
from generals import CONN

def row_number ():
    query = """
select count(*) from tlc_ny.yellow.taxi_trips
    """
    with CONN.connect() as connection:
        result = connection.execute(text(query))
        return result.fetchone()[0]

if __name__ == "__main__":
    print(row_number())
