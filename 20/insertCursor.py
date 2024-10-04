# 1. Using InsertCursor, add in the location of Albritton Bell Tower to our campus geodatabase
# Located at Lat: 30.61312, Lon: -96.34468
# Wrong location at Lat: 30.61320, Lon: -96.34381
import arcpy

# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/20/Campus.gdb"
# Define our tower point location
towerLocation = ('Albritton Bell Tower', (30.61320, -96.34381))
# Define the tower's spatial reference
spatialRef = arcpy.SpatialReference(3857)
# Create a new feature class in the gdb
# arcpy.CreateFeatureclass_management(campus, "Albritton", geometry_type="POINT", spatial_reference=spatialRef)
# Define fields we want in Albritton
fields = (
    ("BldgName", "TEXT", None, None, 50, "", "NULLABLE", "NON_REQUIRED")
)
# Add the fields to Albritton
# for field in fields:
#     arcpy.AddField_management(campus + "/Albritton", "BldgName", "TEXT")
insertCursor = arcpy.da.InsertCursor(campus + "/Albritton", ["BldgName", "SHAPE@XY"])
# array = arcpy.Array([towerLocation])
# feature = arcpy.Polygon(array, spatialRef)
insertCursor.insertRow(towerLocation)

del insertCursor
