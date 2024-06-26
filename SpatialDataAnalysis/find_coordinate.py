"""
Script to find the municipality and department of a given point (latitude, longitude).
"""
from typing import Tuple
import json
import pandas as pd
from shapely.geometry import Point, shape


def get_data(department_path: str, geo_path: str) -> Tuple[pd.DataFrame, dict]:
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
    with open(geo_path, encoding='utf-8') as f:
        municipios_json = json.load(f)
    return deparment_id, municipios_json

def data_polygon(geo_json: dict) -> dict:
    """
    Given a GeoJSON dictionary, returns the same dictionary with the polygons added.
    """
    for feature in geo_json['features']:
        polygon = shape(feature['geometry'])
        # add the polygon to the dictionary
        feature['polygon'] = polygon
    return geo_json


def get_municipio(point_: list, geo_json: dict) -> Tuple[str, str]:
    """
    Given a point (latitude, longitude), returns the name of the municipality it belongs to.

    Args:
    - point (tuple): A tuple containing the latitude and longitude of the point.
    - geo_path (str): The path to the GeoJSON file containing the polygons of the municipalities.

    Returns:
    - str: The name of the municipality the point belongs to."""
    point_ = Point(point_)
    for feature in geo_json['features']:
        if feature['polygon'].contains(point_):
            return feature['properties']['NAM'], feature['properties']['NA3']
    return 'Unknow', 'Unknow'


def get_dpto(dpt_df: pd.DataFrame, id_mun: str) -> str:
    "Given a municipality id, returns the name of the department it belongs to."
    id_mun = id_mun[:2]
    dpto = dpt_df[dpt_df['ID'] == id_mun]
    return dpto['DPTO'].values[0]


def location(point_: list, geo_json: dict, dpt_df: pd.DataFrame) -> Tuple[str, str]:
    """Given a point (latitude, longitude),
    returns the name of the municipality and department it belongs to."""
    mun, id_mun = get_municipio(point_, geo_json)
    if mun == 'Unknow' or id_mun == '0000':
        return mun, id_mun
    dpto = get_dpto(dpt_df, id_mun)
    return mun, dpto


def main(list_coords: list,
         geo_path: str,
         department_path: str) -> list:
    """
    Main function to find the municipality and department of a given point (latitude, longitude).
    """
    department_df, geo_df = get_data(department_path, geo_path)
    geo_df = data_polygon(geo_df)
    list_locations = []
    for point in list_coords:
        list_locations.append(
            point + list(location(point, geo_df, department_df)))
    return list_locations


if __name__ == '__main__':
    # Longitud, latitud
    GEO_PATH = 'datawarehouse/limites_municipales.geojson'
    DPTO_PATH = 'dpto_id.csv'
    TEST_POINT = [[-88.56675753436322, 13.186794959425315],[-88.766764, 13.870447]]
    test_location = main(TEST_POINT, GEO_PATH, DPTO_PATH)
    print(test_location)
