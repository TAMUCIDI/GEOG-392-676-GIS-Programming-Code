import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"

# Define our layer
structures = campus + "/Structures"

# SelectLayerByAttribute doesn't like feature classes; create a feature layer from feature class
arcpy.MakeFeatureLayer_management(structures, "lyr")


# Define our where clause
# where = "[Type] = 'RESEARCH'"
# where = '"Type" LIKE "RESEARCH"'
where = "[NAME] = 'California'"

# Perform a select
arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", where)


