from typing import List
from sqlalchemy.engine.base import Connection

def generate_dates(start_date_: str, end_date_: str) -> List[str]: ...

START_DATE: str
END_DATE: str
DATA_RANGE: List[str]
CONN: Connection