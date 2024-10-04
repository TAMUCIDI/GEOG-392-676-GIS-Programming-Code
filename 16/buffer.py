
import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

# Perform buffer on the wh feature class in our geodatabase
dcGdb = r"C:/tmp/ArcGISPython/DC.gdb"
arcpy.Buffer_analysis(dcGdb + "/wh", dcGdb + "/wh_buffered_bg", .009)