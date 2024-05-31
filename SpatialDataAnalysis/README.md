# Spatial data analysis in Python

In this repository, I will be sharing my work on spatial data analysis in Python.

## List of projects

### - [find_coordinate](https://github.com/gfgh512/my-projects/raw/master/SpatialDataAnalysis/find_coordinate.py)
The goal of this project is to find the location of a given
coordinate. The locations are municipalities in El Salvador,
for each location we have the boundary of the municipality.
below you will find the link to the data source in geojson format.

It's a simple solution to find the location of a given coordinate
using the shapely library.

### - [find_coordinate_geopandas](https://github.com/gfgh512/my-projects/raw/master/SpatialDataAnalysis/find_coordinate_geopandas.py)
Same as the previous project, but using the geopandas library.
This solution is more efficient than the previous one, and is more suitable for large datasets, just need to do some modifications to the code.

#### Data source:

[municipalities](https://www.cnr.gob.sv/geoubicaciones-cnr/2022/agosto/16/L%C3%8DMITES_MUNICIPALES_GEOJSON.zip)
- type: GeoJSON

note:
- departments_id: The departments_id is a short csv file in the project folder, this is because the data source does not have the department_id. You could visit the fallowing URL if you want, but the page does note have ssl certificate, and that is why I don't programatically download the file within the project.
(https://www.cnr.gob.sv/geoubicaciones-cnr/octubre_17/CNR_Geoubicaciones_cantones.json)

#### Libraries used:
- [Json](https://docs.python.org/3/library/json.html)
- [Typing](https://docs.python.org/3/library/typing.html)
- [Shapely](https://shapely.readthedocs.io/en/stable/)
- [Geopandas](https://geopandas.org/)
- [Pandas](https://pandas.pydata.org/)