import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"

# Define our layers
structures = campus + "/Structures"
landuse = campus + "/LandUse"

# Perform a union of two layers
arcpy.Union_analysis([structures, landuse], campus + "/Campus_union", "NO_FID")