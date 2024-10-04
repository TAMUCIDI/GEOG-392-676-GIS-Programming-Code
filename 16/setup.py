import arcpy

# Set our workspace
arcpy.env.workspace = "C:/tmp/ArcGISPython"
arcpy.env.scratchWorkspace = "C:/tmp/ArcGISPython/scratch"

# Create  new geodatabase
folder_path = "C:/tmp/ArcGISPython"
arcpy.CreateFileGDB_management(folder_path, "Test.gdb")
