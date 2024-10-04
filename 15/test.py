import arcpy

inFC = arcpy.GetParameterAsText(0)
outFC = arcpy.GetParameterAsText(1)

# Describe a feature class using arcpy.Describe
desc = arcpy.Describe(inFC)

# If the shapeType is Polygon convert the data to polylines using the 
# FeatureToLine tool, otherwise just copy the data using the CopyFeatures tool.
if desc.shapeType == "Polygon":
    arcpy.FeatureToLine_management(inFC, outFC)
else:
    arcpy.CopyFeatures_management(inFC, outFC)