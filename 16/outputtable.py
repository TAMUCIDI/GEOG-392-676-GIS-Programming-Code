import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

dcGdb = r"C:/tmp/ArcGISPython/DC.gdb"

# Output the attribute table of intersection feature class to a .csv
arcpy.TableToTable_conversion(dcGdb + "/intersection.dbf", "C:/tmp/ArcGISPython", "intersection.csv")
