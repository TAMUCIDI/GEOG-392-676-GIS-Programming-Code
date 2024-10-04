import arcpy

# Set our workspace
arcpy.env.workspace = "C:/tmp/ArcGISPython"
arcpy.env.scratchWorkspace = "C:/tmp/ArcGISPython/scratch"

# Create a new geodatabase
arcpy.CreateFileGDB_management(arcpy.env.workspace, "DC.gdb")

# Create a White House layer from a .csv
whitehouse = arcpy.management.MakeXYEventLayer("wh.csv", "x", "y", "wh")

# Insert the two input layers into the newly created DC.gdb
input_layers = ["removed_trees.shp", whitehouse]
arcpy.FeatureClassToGeodatabase_conversion(input_layers, r"C:/tmp/ArcGISPython/DC.gdb")

# Calculate the distance from the WH to each removed tree, adding the distance as a field in the process
dcGdb = r"C:/tmp/ArcGISPython/DC.gdb"
arcpy.analysis.Near(dcGdb + "/removed_trees", dcGdb + "/wh", None, "NO_LOCATION", "NO_ANGLE", "PLANAR")
