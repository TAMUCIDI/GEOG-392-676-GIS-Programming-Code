import arcpy

arcpy.env.workspace = "C:/tmp/ArcGISPython"
# arcpy.env.scratchWorkspace = "C:/tmp/ArcGISPython"

# arcpy.CreateFileGDB_management(arcpy.env.workspace, "Test.gdb")
arcpy.env.scratchWorkspace = ""

print(arcpy.ListEnvironments())