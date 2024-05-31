"""
Script to find the municipality and department of a given point (latitude, longitude).
"""
from typing import Tuple
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


def get_data(department_path: str, geo_path: str) -> Tuple[gpd.GeoDataFrame, dict]:
    """
    Reads in data from two files and returns a tuple containing a pandas DataFrame and a dictionary.

    Args:
    - department_path (str): The file path to the CSV file containing the municipalities data.
    - geo_path (str): The file path to the JSON file containing the geo data.

    Returns:
    - Tuple[pd.DataFrame, dict]: A tuple containing a pandas DataFrame and a dictionary.
    """
    deparment_id = pd.read_csv(
        department_path, encoding='utf-8', dtype={'ID': str})
    geo_df = gpd.read_file(geo_path)
    return deparment_id, geo_df


def get_municipio(point_: list, geo_df: gpd.GeoDataFrame) -> Tuple[str, str]:
    """
    Given a point (latitude, longitude), returns the name of the municipality it belongs to.

    Args:
    - point (tuple): A tuple containing the latitude and longitude of the point.
    - geo_path (str): The path to the GeoJSON file containing the polygons of the municipalities.

    Returns:
    - str: The name of the municipality the point belongs to."""
    point_ = Point(point_)
    try:
        geo_df = geo_df[geo_df.contains(point_)]
        return geo_df['NAM'].values[0], geo_df['NA3'].values[0]
    except IndexError:
        return 'Unknow', 'Unknow'


def get_department(department_df: pd.DataFrame, id_mun: str) -> str:
    "Given a municipality id, returns the name of the department it belongs to."
    id_mun = id_mun[:2]
    dpto = department_df.loc[department_df['ID'] == id_mun]
    return dpto['DPTO'].values[0]


def location(point_: list,
             geo_df: gpd.GeoDataFrame,
             department_df: pd.DataFrame) -> Tuple[str, str]:
    """Given a point (latitude, longitude),
    returns the name of the municipality and department it belongs to."""
    mun, id_mun = get_municipio(point_, geo_df)
    if mun == 'Unknow' or id_mun == '0000':
        return mun, id_mun
    dpto = get_department(department_df, id_mun)
    return mun, dpto


def main(list_coords: list,
         geo_path: str,
         department_path: str) -> list:
    """
    Main function to find the municipality and department of a given point (latitude, longitude).
    """
    department_df, geo_df = get_data(department_path, geo_path)
    list_locations = []
    for point in list_coords:
        list_locations.append(
            point + list(location(point, geo_df, department_df)))
    return list_locations


if __name__ == '__main__':
    # Longitud, latitud
    GEO_PATH = 'datawarehouse/limites_municipales.geojson'
    DPTO_PATH = 'dpto_id.csv'
    TEST_POINT = [[-88.56675753436322, 13.186794959425315],
                  [-88.766764, 13.870447]]
    test_location = main(TEST_POINT, GEO_PATH, DPTO_PATH)
    print(test_location)
