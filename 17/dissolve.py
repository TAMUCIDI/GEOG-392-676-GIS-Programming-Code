import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"

# Define our layers
structures = campus + "/Structures"

# Perform a clip
arcpy.Dissolve_management(structures, campus + "/Dissolved_structures", "Type")