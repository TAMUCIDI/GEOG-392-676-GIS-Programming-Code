import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"

# Perform a clip
arcpy.Clip_analysis(campus + "/Structures", campus + "/GaragePoints_buffered", campus + "/Clipped_structures")