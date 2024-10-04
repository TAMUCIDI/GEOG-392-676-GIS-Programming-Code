import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"

# Define our layer
structures = campus + "/Structures"

# Define our where clause
where = '"Type" = \'HOUSING TAMU\''

# Perform a select
arcpy.Select_analysis(structures, campus + "/housing", where)
