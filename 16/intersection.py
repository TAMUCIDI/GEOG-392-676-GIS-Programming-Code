import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

dcGdb = r"C:/tmp/ArcGISPython/DC.gdb"

# Perform an intersect on two feature layers inside dcGdb and save the result in the geodatabase
arcpy.Intersect_analysis([dcGdb + "/wh_buffered_bg", dcGdb + "/removed_trees"], dcGdb + "/intersection", "ALL")

